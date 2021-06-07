from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(255))
    valor = db.Column(db.Float(10,2))
    estado = db.Column(db.Boolean())

    def __init__(self, descricao, valor, estado=1):
        self.descricao = descricao
        self.valor = valor
        self.estado = estado
