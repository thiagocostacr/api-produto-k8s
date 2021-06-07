import requests
from flask import jsonify, request
from models import db, Produto
from app import app, db


@app.route('/produto', methods=['GET'])
def listar():
    produtos = Produto.query.filter_by(estado=1).all()
    resultado = retornoHelper(produtos)
    return jsonify(resultado)

@app.route('/produto/<int:id>', methods=['GET'])
def listarId(id):
    produto = Produto.query.filter_by(id = id, estado=1).first()
    return jsonify({'id': produto.id, 'descricao': produto.descricao, 'valor': str(produto.valor)})

@app.route('/produto', methods=['POST'])
def inserir():
    produto = request.json
    nProduto = Produto(produto['descricao'], produto['valor'], 1)
    db.session.add(nProduto)
    db.session.commit()
    return jsonify('produto ' + produto['descricao'] + ' inserido com sucesso!')

@app.route('/produto/<int:id>', methods=['DELETE'])
def excluir(id):
    produto = Produto.query.filter_by(id=id, estado=1).first()
    produto.estado = 0
    db.session.commit()
    return jsonify('produto excluído com sucesso!')

@app.route('/produto', methods=['PUT'])
def atualizar():
    data = request.json
    produto = Produto.query.filter_by(id=data['id'], estado=1).first()
    produto.descricao = data['descricao']
    produto.valor = data['valor']
    db.session.commit()
    return jsonify('produto atualizado com sucesso!')

def retornoHelper(produtos):
    resultados = []
    for produto in produtos:
        resultados.append({'id': produto.id, 'descricao': produto.descricao, 'valor': str(produto.valor)})
    return resultados
