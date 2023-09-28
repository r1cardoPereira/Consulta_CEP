



# Bem-vindo ao Consulta CEP

Este é um projeto simples que permite buscar informações de endereço a partir de um CEP usando a API ViaCEP.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python 3 e o pip instalados em seu sistema.

## Instalação

* Clone o repositório do projeto:

```
git clone https://github.com/r1cardopereira/consulta_cep.git
```

* Crie um ambiente virtual para o projeto:

```
python3 -m venv env
```

* Ative o ambiente virtual:

```
source env/bin/activate
```

* Instale as dependências do projeto:

```
pip install -r requirements.txt
```

## Comandos

* `uvicorn consulta_cep.main:app --reload` - Inicia o servidor web.
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

## Observações:
Projeto desenvolvido em ambiente Linux.

No meu caso, o MongoDB está rodando em um container Docker. Para que o projeto funcione corretamente, é necessário que o container esteja em execução.

se você não tiver o MongoDB instalado em seu sistema, pode usar o seguinte comando para iniciar um container Docker com o MongoDB:

```
docker run --name mongodb -p 27017:27017 -d mongo
```
Mude a linha no modulo: `mongodb.py` para conectar ao seu banco de dados.

De:
```	
MONGODB_CLIENT = MongoClient('localhost', 27017)
```
Para:
```	
MONGODB_CLIENT = MongoClient('mongodb', 27017)
```
e adicione a seguinte linha no arquivo `/etc/hosts`:

```
127.0.0.1 mongodb
```
## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.