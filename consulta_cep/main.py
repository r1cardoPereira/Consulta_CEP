import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/address/{cep}")
async def search_address_by_cep(cep: str) -> dict:
    """
    Busca o endereço correspondente ao CEP informado na API ViaCEP.
    >>> search_address_by_cep("69910-270")
    {'cep': '69910-270', 'logradouro': 'Rua Rio Grande do Sul', 'complemento': '', 'bairro': 'João Eduardo I', 'localidade': 'Rio Branco', 'uf': 'AC', 'ibge': '1200401', 'gia': '', 'ddd': '68', 'siafi': '1200'}

    Args:
        cep (str): O CEP a ser pesquisado.

    Returns:
        dict: Um dicionário contendo as informações do endereço correspondente ao CEP informado.

    Raises:
        HTTPException: Se o CEP informado não for encontrado ou se ocorrer um erro na requisição.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="CEP não encontrado")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Erro na requisição")

    return response.json()



