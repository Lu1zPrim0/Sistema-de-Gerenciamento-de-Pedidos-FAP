from . import db
class Produto(db.Model):

    __tablename__ = 'produtos'

class Produto(db.Model):
    produto_id = db.Column(db.Integer, primary_key=True)
    produto_nome = db.Column(db.String(100), nullable=False)
    dp_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Produto {self.produto_nome}>'
