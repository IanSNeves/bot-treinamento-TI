from flask import Flask
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from database import db
from routes import main_bp 

load_dotenv()

app = Flask(__name__)

# --- Configuração do Banco de Dados ---
bdSenha = os.getenv('BD_SECRET_KEY')
if not bdSenha:
    raise ValueError("A variável BD_SECRET_KEY não foi encontrada.")

bdSenha_tratada = quote_plus(bdSenha)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://usuario_flask:{bdSenha_tratada}@localhost/chatbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = bdSenha

# Inicialização do Banco
db.init_app(app)

# Registro das Rotas (Blueprint)
app.register_blueprint(main_bp)

# Criação das tabelas (se não existirem)
with app.app_context():
    from models import BaseDeConhecimento 
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)