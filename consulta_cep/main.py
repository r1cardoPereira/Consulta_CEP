import logging
import requests
from pymongo import errors
from typing import Any, List, Optional

from fastapi import FastAPI, Path, Request, status
from fastapi.responses import JSONResponse

from consulta_cep import schemas
from bootstrap import mongodb

logger = logging.getLogger(__name__)

app = FastAPI()
mongodb.install(app)


async def save_address(address: dict) -> None:
    """
    Salva o endereço fornecido no banco de dados.

    Args:
        address (dict): Um dicionário contendo as informações do endereço a ser salvo.

    Returns:
        None

    """
    app.db.insert_one(address)


class CepNotFoundException(Exception):
    """
    Exceção lançada quando um CEP (código postal brasileiro) não é encontrado.    
    """
    pass


@app.exception_handler(CepNotFoundException)
async def cep_not_found_handler(request: Request, exc: CepNotFoundException):
    """
    Lida com caso em que o CEP não é encontrado.

    Args:
       request (Request): O objeto de requisição.
        exc (CepNotFoundException): O objeto de exceção.

    Returns:
       JSONResponse: Uma resposta JSON com um código de status 404 e uma mensagem indicando que o CEP não foi encontrado.
    """
    return JSONResponse(status_code=404, content={"message": "Cep não encontrado"})


@app.get("/address", response_model=schemas.AddressOutput)
async def search_address(state: Optional[str] = None):
    """
    Searches for addresses in the database based on the given state.

    Examples:
        >>>> search_address("RJ")
        return:
            [
                {
                "cep": "23052-350",
                "logradouro": "Rua Henri Dunant",
                "complemento": "",
                "bairro": "Campo Grande",
                "localidade": "Rio de Janeiro",
                "uf": "RJ",
                "ddd": "21",
                },
            ]

    Args:
        state (Optional[str]): The state to search for addresses in. If None, returns all addresses.

    Returns:
        List[Dict]: A list of dictionaries representing the addresses found in the database.
    """
    if state:
        return list(app.db.find({"uf": state}))

    return list(app.db.find({}))


@app.get("/address/{cep}", response_model=schemas.AddressOutput)
async def search_address_by_cep(cep: str) -> dict:
    """
    Busca o endereço correspondente ao CEP informado na API ViaCEP e salva no banco de dados.

    Examples:
        >>> search_address_by_cep("23052-350")
        return:
            {
            "cep": "23052-350",
            "logradouro": "Rua Henri Dunant",
            "complemento": "",
            "bairro": "Campo Grande",
            "localidade": "Rio de Janeiro",
            "uf": "RJ",
            "ibge": "3304557",
            "gia": "",
            "ddd": "21",
            "siafi": "6001"
            }

    Args:
        cep (str): O CEP a ser pesquisado.

    Returns:
        dict: Um dicionário contendo as informações do endereço correspondente ao CEP informado.

    Exceptions:
        HTTPException: Se o CEP informado não for encontrado ou se ocorrer um erro na requisição.
    """
    address = app.db.find_one({"cep": cep})

    if not address:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        address = response.json()

        if "erro" in address:
            raise CepNotFoundException()

        await save_address(address)
    return address


@app.post("/address", response_model=schemas.AddressOutput, status_code=201)
async def create_address(address: schemas.AddressInput):
    """
    Crie um novo endereço no banco de dados.

    Examples:
        >>> create_address(schemas.AddressInput(
                cep="23052-350", 
                logradouro="Rua Henri Dunant", 
                complemento="", 
                bairro="Campo Grande", 
                localidade="Rio de Janeiro", 
                uf="RJ", 
                ibge="3304557", 
                gia="", 
                ddd="21", 
                siafi="6001"
                )
            )

    Args:
        address (schemas.AddressInput): O endereço a ser criado.

    Returns:
        schemas.AddressInput: O endereço criado..

    Raises:
        JSONResponse: Caso o CEP já esteja cadastrado no banco de dados.
    """
    try:
        await save_address(address.model_dump())
        return address

    except errors.DuplicateKeyError:
        return JSONResponse(status_code=409, content={"message": "Cep já cadastrado"})


@app.put("/address/{cep}", status_code=status.HTTP_204_NO_CONTENT)
async def update_address(cep: str, address: schemas.AddressInput):
    """
    Atualize um endereço existente no banco de dados com o CEP fornecido.

    Examples:
        >>> update_address("23052-350", schemas.AddressInput(
                cep="23052-350", 
                logradouro="Rua Henri Dunant", 
                complemento="", 
                bairro="Campo Grande", 
                localidade="Rio de Janeiro", 
                uf="RJ", 
                ibge="3304557", 
                gia="", 
                ddd="21", 
                )
            )

    Args:
        cep (str): O CEP do endereço a ser atualizado.
        address (schemas.AddressInput): os dados de endereço atualizados.

    Returns:
        None
    """
    old_address = app.db.find_one({"cep": cep})
    print(f'Old_address: {old_address}')
    update_data = {"$set": address.model_dump()}

    print(f"Updating address {old_address} with {update_data}")
    print(f"Update_data: {update_data}")
    app.db.update_one(old_address, update_data)


@app.get("/addresses", response_model=List[schemas.AddressOutput])
async def list_addresses():
    """
    Lista todos os endereços no banco de dados.

    Returns:
        List[schemas.Address]: Uma lista de objetos Address contendo os endereços no banco de dados.
    """
    addresses = []
    for address in app.db.find():
        addresses.append(schemas.AddressOutput(**address))
    return addresses
