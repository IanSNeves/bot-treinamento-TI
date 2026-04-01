from flask import request, Blueprint, render_template
from services import bot
from flask_login import login_required

main_bp = Blueprint('main', __name__)


@main_bp.route('/chat', methods=['GET'])
@login_required
def chat():
    return render_template('chat.html')


@main_bp.route('/menu', methods=['GET'])
@login_required
def menu():
    return render_template('menu.html')


@main_bp.route('/enviar_mensagem', methods=['POST'])
@login_required
def enviar_mensagem():
    # HTMX envia como form data, não JSON → usar request.form
    user_message = request.form.get('user_message', '').strip()

    if not user_message:
        return '<div class="message message--bot"><p>Nenhuma mensagem recebida.</p></div>', 400

    bot_response = bot(user_message)

    # Retorna os dois balões para o HTMX inserir via hx-swap="beforeend"
    return f'''
<div class="message message--user">
    <p>{user_message}</p>
</div>
<div class="message message--bot">
    {bot_response}
</div>
'''