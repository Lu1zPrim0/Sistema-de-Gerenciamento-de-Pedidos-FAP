from . import db 

class Pedido(db.Model):
    pedido_id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Pedido {self.pedido_id}>'
