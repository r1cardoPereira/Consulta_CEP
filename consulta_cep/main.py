import requests
from typing import Any

from fastapi import FastAPI, Path, HTTPException

from consulta_cep import schemas
from bootstrap import mongodb

app = FastAPI()
mongodb.install(app)


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

        await save_address(address)
    return address


async def save_address(address: dict) -> None:
    """
    Salva o endereço fornecido no banco de dados.

    Args:
        address (dict): Um dicionário contendo as informações do endereço a ser salvo.

    Returns:
        None

    """
    app.db.insert_one(address)
