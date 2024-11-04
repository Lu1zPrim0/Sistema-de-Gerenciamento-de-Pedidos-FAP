from flask_sqlalchemy import SQLAlchemy

# Instancia do SQLAlchemy
db = SQLAlchemy()

# Importação dos modelos após a criação da instância do banco de dados
from .produto import Produto
from .usuario import Usuario
from .cliente import Cliente
from .pedido import Pedido
from .detalhePedido import DetalhePedido
