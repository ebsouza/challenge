import unittest
import os
import json
from app import create_app
from mongoengine import connect

def createEstabelecimentoJSON():
    json_file = {}
    json_file['nome'] = "Batata & Cia"
    json_file['cnpj'] = "45.283.163/0001-67"
    json_file['dono'] = "Roberto Campos"
    json_file['telefone'] = "+55(21)3323-7786"
    return json_file

def createTransacaoJSON():
    json_file = {}
    json_file['estabelecimento'] = "45.283.163/0001-67"
    json_file['cliente'] = "094.214.930-01"
    json_file['valor'] = 32.50
    json_file['descricao'] = "Almoco em restaurante chique pago via Shipay!"
    return json_file   

class challengeTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""
    config_name= 'testing'

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(challengeTestCase.config_name)
        self.client = self.app.test_client

    def test_app_exists(self):
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    """
    '/api/v1/estabelecimento' [POST]
    """
    #JSON estabelecimento no formato aceito
    def test_insert_estabelecimento_ok(self):
        
        json_file = createEstabelecimentoJSON()

        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 200)

    #Erro no conteúdo do campo CNPJ
    def test_insert_estabelecimento_cnpj_error(self):
        
        json_file = createEstabelecimentoJSON()
        json_file['cnpj'] = "45.283.163/0001-672"

        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

    #JSON vazio
    def test_insert_estabelecimento_empty_json(self):
        
        json_file = {}

        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Falta dos campos requeridos
    def test_insert_estabelecimento_missing_fields(self):
        
        json_file = createEstabelecimentoJSON()
        json_file.pop('nome', None)
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('cnpj', None)
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('dono', None)
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('telefone', None)
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Falta de valores requeridos
    def test_insert_estabelecimento_missing_values(self):
        
        json_file = createEstabelecimentoJSON()
        json_file['nome'] = None
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['cnpj'] = None
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['dono'] = None
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['telefone'] = None
        res = self.client().post('/api/v1/estabelecimento', json=json_file)
        self.assertEqual(res.status_code, 400)


    """
    '/api/v1/transacao' [POST]
    """
    #JSON transacao no formato aceito
    def test_insert_transacao_ok(self):
        
        json_file = createTransacaoJSON()

        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 200)

    #Erro no formato do CNPJ
    def test_insert_transacao_cnpj_error(self):
        
        json_file = createTransacaoJSON()
        json_file["estabelecimento"] = "45.283.163/0001-621"

        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Erro no formato do CPF
    def test_insert_transacao_cpf_error(self):
        
        json_file = createTransacaoJSON()
        json_file["cliente"] = "094.214.930-101"

        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

    #JSON vazio
    def test_insert_transacao_empty_json(self):
        
        json_file = {}

        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Falta dos campos requeridos
    def test_insert_transacao_missing_fields(self):
        
        json_file = createEstabelecimentoJSON()
        json_file.pop('estabelecimento', None)
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('cliente', None)
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('valor', None)
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file.pop('descricao', None)
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Falta de valores requeridos
    def test_insert_transacao_missing_values(self):
        
        json_file = createEstabelecimentoJSON()
        json_file['estabelecimento'] = None
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['cliente'] = None
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['valor'] = None
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

        json_file = createEstabelecimentoJSON()
        json_file['descricao'] = None
        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)

    #Campo valor com texto
    def test_insert_transacao_wrong_field(self):
        
        json_file = createEstabelecimentoJSON()
        json_file["valor"] = "A"

        res = self.client().post('/api/v1/transacao', json=json_file)
        self.assertEqual(res.status_code, 400)


    """
    '/api/v1/transacao/estabelecimento' [GET]
    """
    #Verificação do status code
    def test_get_estabelecimento_ok(self):

        #Limpa o banco 
        db = connect('test')
        db.drop_database('test')
        estabelecimento_json = createEstabelecimentoJSON()
        self.client().post('/api/v1/estabelecimento', json=estabelecimento_json)

        cnpj = estabelecimento_json["cnpj"]

        url = "/api/v1/transacao/estabelecimento?cnpj={}".format(cnpj)
        res = self.client().get(url)
        self.assertEqual(res.status_code, 200)

        #Limpa o banco
        db.drop_database('test')

    #Consistencia da operação de inserção do estabelecimento e transações
    def test_get_estabelecimento_json(self):

        #Limpa o banco 
        db = connect('test')
        db.drop_database('test')

        #Dados
        estabelecimento_json = createEstabelecimentoJSON()
        transacao_1_json = createTransacaoJSON()
        transacao_2_json = createTransacaoJSON()

        transacao_2_json["cliente"] =  "094.214.930-10"
        transacao_2_json["valor"] =  20.50

        #Insercao dos dados no banco
        self.client().post('/api/v1/estabelecimento', json=estabelecimento_json)
        self.client().post('/api/v1/transacao', json=transacao_1_json)
        self.client().post('/api/v1/transacao', json=transacao_2_json)

        #Request
        cnpj = estabelecimento_json["cnpj"]
        url = "/api/v1/transacao/estabelecimento?cnpj={}".format(cnpj)
        res = self.client().get(url)
        json_response = json.loads(res.data)

        #Preapração para a comparação
        transacao_1_json.pop('estabelecimento', None)
        transacao_2_json.pop('estabelecimento', None)

        #Verificação da consistência
        self.assertEqual(estabelecimento_json, json_response["estabelecimento"])
        self.assertTrue(transacao_1_json in json_response["recebimentos"])
        self.assertTrue(transacao_2_json in json_response["recebimentos"])

        valor = transacao_1_json["valor"] + transacao_2_json["valor"]
        self.assertEqual(valor, json_response["total"])

        #Remove 
        db.drop_database('test')

        self.assertEqual(res.status_code, 200)

    #Url passada com parâmetro errado
    def test_get_estabelecimento_wrong_cnpj(self):

        cnpj = "45.283.163/0001-67"

        url = "/api/v1/transacao/estabelecimento?A={}".format(cnpj)
        res = self.client().get(url)
        self.assertEqual(res.status_code, 400)

        url = "/api/v1/transacao/estabelecimento?cnpj?{}".format(cnpj)
        res = self.client().get(url)
        self.assertEqual(res.status_code, 400)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()