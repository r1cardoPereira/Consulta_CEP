# Main

O arquivo `main.py` é o ponto de entrada da aplicação. Ele define as rotas da API e inicia o servidor web usando o framework FastAPI.

A rota principal `/` retorna uma mensagem de boas-vindas. A rota `/address/{cep}` é usada para buscar informações de endereço a partir de um CEP usando a API ViaCEP. A rota `/docs` é usada para acessar a documentação da API gerada automaticamente pelo framework Swagger UI.

O arquivo `main.py` também define uma conexão com o banco de dados MongoDB usando a biblioteca PyMongo. O banco de dados é usado para armazenar os dados de endereço pesquisados na API.

Além disso, o arquivo `main.py` importa os modelos de dados definidos no módulo `schemas.py` e usa-os para validar os dados de entrada e saída da API.

:::main