



# Bem-vindo ao Consulta CEP

Este é um projeto simples que permite buscar informações de endereço a partir de um CEP usando a API ViaCEP.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python 3 e o pip instalados em seu sistema.

## Instalação

1. Clone o repositório do projeto:

```
git clone https://github.com/r1cardopereira/consulta_cep.git
```

2. Crie um ambiente virtual para o projeto:

```
python3 -m venv env
```

3. Ative o ambiente virtual:

```
source env/bin/activate
```

4. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

## Comandos

* `uvicorn main:app --reload` - Inicia o servidor web.
* `pytest` - Executa os testes automatizados.

## Estrutura do projeto
```
    
    ├── README.md
    ├── bootstrap
    │   ├── __init__.py
    │   └── mongodb.py
    ├── consulta_cep
    │   ├── __init__.py   
    │   ├── main.py
    │   └── schemas.py
    └── tests
        └── __init__.py
```

## Documentação

A documentação do projeto está disponível em [localhost:8000/docs](http://localhost:8000/docs) após iniciar o servidor web.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.