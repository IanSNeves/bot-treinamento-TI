from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class BaseDeConhecimento(db.Model):
    __tablename__ = 'base_de_conhecimento'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)