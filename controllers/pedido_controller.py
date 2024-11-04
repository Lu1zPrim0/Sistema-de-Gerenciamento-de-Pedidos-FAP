from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Pedido

pedido_bp = Blueprint('pedidos', __name__)

@pedido_bp.route('/pedidos', methods=['POST'])
def criar_pedido():
    pedido = request.json
    data_compra = datetime.strptime(pedido['data_compra'], '%Y-%m-%d').date()
    novo_pedido = Pedido(data_compra=data_compra, cliente_id=pedido['cliente_id'])
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'id': novo_pedido.pedido_id, 'data_compra': novo_pedido.data_compra}), 201

@pedido_bp.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{'ID': p.pedido_id, 'DataCompra': p.data_compra, 'ClienteID': p.cliente_id} for p in pedidos]), 200

@pedido_bp.route('/pedidos/<int:id>', methods=['GET'])
def obter_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    return jsonify({
        'ID': pedido.pedido_id,
        'DataCompra': pedido.data_compra,
        'ClienteID': pedido.cliente_id
    }), 200

@pedido_bp.route('/pedidos/<int:id>', methods=['PUT'])
def atualizar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    dados = request.json
    pedido.data_compra = datetime.strptime(dados['data_compra'], '%Y-%m-%d').date()
    pedido.cliente_id = dados.get('cliente_id', pedido.cliente_id)
    db.session.commit()
    return jsonify({
        'ID': pedido.pedido_id,
        'DataCompra': pedido.data_compra,
        'ClienteID': pedido.cliente_id
    }), 200

@pedido_bp.route('/pedidos/<int:id>', methods=['DELETE'])
def deletar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensagem': 'Pedido deletado com sucesso'}), 200
