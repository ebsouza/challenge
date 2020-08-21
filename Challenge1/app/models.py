import mongoengine as me

#https://flask.palletsprojects.com/en/1.1.x/patterns/mongoengine/

class Transacao(me.EmbeddedDocument):

    #estabelecimento = me.StringField(required=True)
    cliente = me.StringField(required=True)
    valor = me.DecimalField(required=True)
    descricao = me.StringField(required=True)

class Estabelecimento(me.EmbeddedDocument):

    nome = me.StringField(required=True)
    cnpj = me.StringField(required=True)
    dono = me.StringField(required=True)
    telefone = me.StringField(required=True)

class Registro(me.Document):
    estabelecimento = me.EmbeddedDocumentField(Estabelecimento)
    recebimentos = me.ListField( me.EmbeddedDocumentField(Transacao) )
    total = me.DecimalField()

