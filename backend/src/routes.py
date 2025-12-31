from flask import Flask,render_template, request, Response, Blueprint
from services import bot

main_bp = Blueprint('main', __name__)

@main_bp.route('/') #Rotas html principal
def index():
    return render_template('base.html')

#Rotas para os conteudos da pagina (htmx)

@main_bp.route('/menu')
def menu():
    return render_template('menu.html')

@main_bp.route('/chat', methods=['GET'])
def chat():
    prompt = request.args.get('msg')
    if prompt:
        resposta = bot(prompt)
    return render_template('chat.html')

@main_bp.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    user_message = request.form.get('user_message')
    bot_response = bot(user_message)
    html_user = f'<div class="message message--user"><p>{user_message}</p></div>'
    html_bot = f'<div class="message message--bot"><p>{bot_response}</p></div>'
    
    return html_user + html_bot    