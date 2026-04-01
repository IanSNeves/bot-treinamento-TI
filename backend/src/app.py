from flask import Flask, render_template
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from database import db
from routes.routes import main_bp 
from routes.auth import auth_bp
from flask_login import LoginManager, login_required
from models import Usuarios


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

# --- Configuração do Flask-Login ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login' # Rota para a qual usuários não logados são redirecionados

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

# Inicialização do Banco
db.init_app(app)

# Registro das Rotas
app.register_blueprint(main_bp, url_prefix='/api') # API do chat
app.register_blueprint(auth_bp) # Rotas de autenticação (/login, /logout)

@app.route('/')
@login_required
def index():
    return render_template('base.html')

# Criação das tabelas
with app.app_context():
    from models import BaseDeConhecimento
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)