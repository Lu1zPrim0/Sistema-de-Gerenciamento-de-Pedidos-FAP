
from . import db    

class Categoria(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    cliente_nome = db.Column(db.String(50), nullable=False)
    cliente_email = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f'<Categoria {self.nome}>'
