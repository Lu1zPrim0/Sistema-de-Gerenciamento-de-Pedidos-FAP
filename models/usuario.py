from . import db

class Usuario(db.Model):

    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_nome = db.Column(db.String(100), nullable=False)
    usuario_senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.nome}>'
