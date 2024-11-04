from flask import Blueprint, request, jsonify
from models import db, Cliente

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    cliente = request.json
    novo_cliente = Cliente(cliente_nome=cliente['cliente_nome'], cliente_email=cliente['cliente_email'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'id': novo_cliente.cliente_id, 'nome': novo_cliente.cliente_nome, 'email': novo_cliente.cliente_email}), 201

@cliente_bp.route('/clientes', methods=['GET'])
def listarClientes():
    clientes = Cliente.query.all()
    return jsonify([{'ID': c.cliente_id, 'Nome': c.cliente_nome} for c in clientes]), 200

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obter_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify({'ID': cliente.cliente_id, 'Nome': cliente.cliente_nome, 'Email': cliente.cliente_email}), 200

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    dados = request.json
    cliente.cliente_nome = dados.get('cliente_nome', cliente.cliente_nome)
    cliente.cliente_email = dados.get('cliente_email', cliente.cliente_email)
    db.session.commit()
    return jsonify({'ID': cliente.cliente_id, 'Nome': cliente.cliente_nome, 'Email': cliente.cliente_email}), 200

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensagem': 'Cliente deletado com sucesso'}), 200
