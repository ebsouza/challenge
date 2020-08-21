from flask import current_app, request, jsonify
import re
import json

#BluePrint 
from . import main

#Modelos
from ..models import Estabelecimento, Transacao, Registro

#Métodos auxiliares
from ..aux import validate_request_json, cnpj_checker, cpf_checker

@main.route('/index')
@main.route('/')
def index():
    return "Hello Shipay"

@main.route('/api/v1/estabelecimento', methods=['POST'])
def registro():

    #Carregamento do JSON
    try:
        file_json = request.get_json()
    except Exception as e:
        error = 'Nao foi possivel abrir o JSON'
        print(error + 'Motivo: %s' % (e))
        return error, 400

    #Validacao do JSON
    fields = ["nome", "cnpj", "dono", "telefone"]
    if not validate_request_json(file_json, fields):
        return "JSON invalido", 400

    #Dados
    nome = file_json["nome"]
    cnpj = file_json["cnpj"]
    dono = file_json["dono"]
    telefone = file_json["telefone"]

    if not cnpj_checker(cnpj):
        return "CNPJ invalido", 400

    registro = Registro()
    registro.estabelecimento = Estabelecimento(nome=nome, cnpj=cnpj, dono=dono, telefone=telefone)
    registro.recebimentos = []
    registro.total = 0.0
    registro.save()

    return "Estabelecimento cadastrado", 200


@main.route('/api/v1/transacao', methods=['POST'])
def post_pedido():
    
    #Carregamento do JSON
    try:
        file_json = request.get_json()
    except Exception as e:
        error = 'Cant open Json.'
        print(error + 'Reason: %s' % (e))
        return error, 400

    #Validacao do JSON
    fields = ["cliente", "estabelecimento", "valor", "descricao"]
    if not validate_request_json(file_json, fields):
        return "JSON invalido", 400

    #Resposta
    response_json = {}
    status_code = 0

    #Dados
    cliente = file_json['cliente']
    cnpj = file_json['estabelecimento']
    try:
        valor = float(file_json['valor'])
    except:
        return jsonify( response_json ), 400
    descricao = file_json['descricao']
    
    if ( cpf_checker(cliente) and cnpj_checker(cnpj) ):   
        #Atualiza o campo total
        Registro.objects(estabelecimento__cnpj=cnpj).update_one(inc__total=valor)

        #Adiciona a nova transacao ao Registro
        transacao = Transacao(cliente=cliente, valor=valor, descricao=descricao)
        Registro.objects(estabelecimento__cnpj=cnpj).update_one(push__recebimentos=transacao)

        response_json['aceito'] = True
        status_code = 200
    else:
        response_json['aceito'] = False
        status_code = 400

    return jsonify( response_json ), status_code
  

@main.route('/api/v1/transacao/estabelecimento', methods=['GET'])
def get_pedido():

    cnpj = request.args.get('cnpj')
    
    #Verificação do campo cnpj
    if cnpj == None:
        return "CNPJ vazio", 400

    #Validação do CNPJ
    if not cnpj_checker(cnpj):
        return "CNPJ invalido", 400

    #Recuperar o JSON no banco
    objects = Registro.objects(estabelecimento__cnpj=cnpj)

    response = json.loads(objects.to_json())
    response[0].pop('_id', None)

    return jsonify( response[0] ), 200


