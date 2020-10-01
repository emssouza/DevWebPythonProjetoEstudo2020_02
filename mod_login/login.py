# coding: utf-8

from flask import Blueprint, render_template, request,  redirect, url_for, session
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route ("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route ("/login", methods=['GET', 'POST'])
def validaLogin():
    _name = request.form['usuario']
    _pass = request.form['senha']
    if _name == "abc" and _pass == "Bolinhas":
        # abre a aplicação na tela home
        session.clear()
        # registra ‘usuario’ na sessão, armazenando o login do usuário
        session['usuario'] = _name
        return redirect(url_for('home.home'))
    else:
        # retorna para a tela de login
        return redirect(url_for('login.login', falhaLogin=1))

@bp_login.route ("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('usuario',None)
    session.clear()
    return redirect(url_for('login.login'))

def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if'usuario' not in session:
            return redirect(url_for('login.login', falhaSessao=1))
        else:
            return f(*args, **kwargs)
    return decorated_function