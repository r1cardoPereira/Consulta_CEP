
# Consulta CEP

Este é um projeto simples que permite buscar informações de endereço a partir de um CEP usando a API ViaCEP.

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para executar o servidor web, execute o seguinte comando:

```
uvicorn consulta_cep.main:app --reload
```
## Observações:
Projeto desenvolvido em ambiente Linux.

No meu caso, o MongoDB está rodando em um container Docker. Para que o projeto funcione corretamente, é necessário que o container esteja em execução.

se você não tiver o MongoDB instalado em seu sistema, pode usar o seguinte comando para iniciar um container Docker com o MongoDB:

```
docker run --name mongodb -p 27017:27017 -d mongo
```
*Mude a linha no pacote Bootstrap no `mongodb.py` para conectar ao seu banco de dados.

```	
MONGODB_CLIENT = MongoClient('localhost', 27017)
```
Para
```	
MONGODB_CLIENT = MongoClient('mongodb', 27017)
```
e adicione a seguinte linha no arquivo `/etc/hosts`:

```
127.0.0.1 mongodb
```


Em seguida, acesse o seguinte URL em seu navegador:

```
http://localhost:8000/address/{cep}
```

Substitua `{cep}` pelo CEP que deseja pesquisar.

## Para mais informações sobre a API, acesse a documentação:

[Documentação Completa](https://r1cardopereira.github.io/consulta-cep/)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.