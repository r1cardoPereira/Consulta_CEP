from pydantic import BaseModel
from typing import Optional


class AddressInput(BaseModel):
    """
    Representa os dados de entrada para um endereço brasileiro.

    Atributos:
        cep (str): O CEP do endereço.
        logradouro (str): O nome da rua do endereço.
        complemento (Optional[str]): O complemento do endereço (por exemplo, número do apartamento).
        bairro (str): O bairro do endereço.
        localidade (str): A cidade do endereço.
        uf (str): O estado do endereço.
        ibge (str): O código IBGE do endereço.
        gia (int): O código GIA do endereço.
        ddd (int): O código DDD do endereço.
    """
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
    ibge: str
    gia: int
    ddd: int


class AddressOutput(BaseModel):
    """
    Representa os dados de saída para um endereço brasileiro.

    Atributos:
        cep: str com o CEP do endereço.
        logradouro: str com o nome do logradouro do endereço.
        complemento: str opcional com informações adicionais sobre o endereço.
        bairro: str com o nome do bairro do endereço.
        localidade: str com o nome da cidade do endereço.
        uf: str com a sigla do estado do endereço.
    """
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
