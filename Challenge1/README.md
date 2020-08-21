## Challenge 1

1 - Start no docker do MongoDB

```shell
$ docker run -d -p 27017:27017 --name mongodb --rm mongo:4.2.6-bionic
```
2 - Start na API

```shell
#Criação do ambiente
$ python3 -m venv Challenge
$ source Challenge/bin/activate
$ (Challenge) pip3 install --upgrade pip
$ (Challenge) pip3 install Flask==1.1.2 flask-mongoengine==0.9.5 requests==2.24.0
```

```shell
#Start na API
$ (Challenge) export FLASK_APP=run.py
$ (Challenge) flask run
```

3 - Endpoints

3.1 - Cadastro de estabelecimento
http://localhost:5000/api/v1/estabelecimento 

Campos do JSON = nome, cnpj, dono, telefone

3.2 - Cadastro de transação
http://localhost:5000/api/v1/transacao 

Campos do JSON = cliente, estabelecimento, valor, descricao

3.3 - Repuração de dados do estabelecimento
http://localhost:5000/api/api/v1/transacoes/estabelecimento?cnpj= 

Obs: Há códigos em python com exemplos de requisição em 'client/client.py'


4 - Testes

Total de 17 casos.

```shell
$ (Challenge) python test.py
```