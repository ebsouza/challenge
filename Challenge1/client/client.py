 
import requests 
import json
from mongoengine import connect

URL = "http://localhost:5000/"


#http://localhost:5000/api/v1/estabelecimento [POST]
def insert_estabelecimento():
    resource = URL + 'api/v1/estabelecimento'
    json_file = {}
    json_file['nome'] = "Batata"
    json_file['cnpj'] = "55.283.163/0001-67"
    json_file['dono'] = "Roberto Campos"
    json_file['telefone'] = "3343-3386"

    r = requests.post(url = resource , json = json_file)
    print(r)

#http://localhost:5000/api/v1/transacao [POST]
def insert_transacao():
    resource = URL + 'api/v1/transacao'
    json_file = {}
    json_file['estabelecimento'] = "55.283.163/0001-67"
    json_file['cliente'] = "194.214.930-01"
    json_file['valor'] = 27.50
    json_file['descricao'] = "Almoço em restaurante chique pago via Shipay!"

    r = requests.post(url = resource , json = json_file)
    r = r.json()
    print(r)

#http://localhost:5000/api/api/v1/transacoes/estabelecimento?cnpj= [GET]
def get_transacao():
    resource = URL + 'api/v1/transacao/estabelecimento?cnpj=55.283.163/0001-67'
    r = requests.get(url = resource)
    print(r)

# ------------------------- #
#insert_estabelecimento()
#insertTransacao()
get_transacao()