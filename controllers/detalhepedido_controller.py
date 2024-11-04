from flask import Blueprint, request, jsonify
from models import db, Pedido, Produto, DetalhePedido #em detalhes não fiz update pela logica de o produto em andamento não ser alterado

detalhePedido_bp = Blueprint('detalhepedidos', __name__)

# Criar um novo detalhe de pedido (Create)
@detalhePedido_bp.route('/detalhepedidos', methods=['POST'])
def criar_detalhe_pedidos():
    detalhepedido = request.json
    novo_detalhe_pedido = DetalhePedido(dp_quantidade=detalhepedido['dp_quantidade'],
                                        dp_preco=detalhepedido['dp_preco'],
                                        dp_desconto=detalhepedido['dp_desconto'],
                                        dp_pedido_id=detalhepedido['dp_pedido_id'],
                                        dp_produto_id=detalhepedido['dp_produto_id'])
    
    db.session.add(novo_detalhe_pedido)
    db.session.commit()
    return jsonify({'id': novo_detalhe_pedido.dp_id}), 201

@detalhePedido_bp.route('/detalhepedidos', methods=['GET'])
def listar_detalhes_pedidos():
    detalhes = DetalhePedido.query.all()
    return jsonify([
        {
            'id': detalhe.dp_id,
            'quantidade': detalhe.dp_quantidade,
            'preco': detalhe.dp_preco,
            'desconto': detalhe.dp_desconto,
            'pedido_id': detalhe.dp_pedido_id,
            'produto_id': detalhe.dp_produto_id
        }
        for detalhe in detalhes
    ]), 200

@detalhePedido_bp.route('/detalhepedidos/<int:id>', methods=['GET'])
def obter_detalhe_pedido(id):
    detalhe = DetalhePedido.query.get_or_404(id)
    return jsonify({
        'id': detalhe.dp_id,
        'quantidade': detalhe.dp_quantidade,
        'preco': detalhe.dp_preco,
        'desconto': detalhe.dp_desconto,
        'pedido_id': detalhe.dp_pedido_id,
        'produto_id': detalhe.dp_produto_id
    }), 200

@detalhePedido_bp.route('/detalhepedidos/<int:id>', methods=['DELETE'])
def deletar_detalhe_pedido(id):
    detalhe = DetalhePedido.query.get_or_404(id)
    db.session.delete(detalhe)
    db.session.commit()
    return jsonify({'mensagem': 'Detalhe do pedido deletado com sucesso'}), 200
