from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import Usuarios

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('password')

        if not username or not senha:
            flash('Usuário e senha são obrigatórios.')
            return redirect(url_for('auth.login'))

        user = Usuarios.query.filter_by(username=username).first()

        if not user or not user.check_password(senha):
            flash('Usuário ou senha inválidos. Por favor, tente novamente.')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('index')) # Redireciona para a página principal (/)

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.')
    return redirect(url_for('auth.login'))