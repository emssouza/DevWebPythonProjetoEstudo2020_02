# coding: utf-8

from flask import Blueprint, render_template, request,  redirect, url_for, session
from functools import wraps
from mod_cliente.clienteBD import Clientes
import hashlib
from funcoes import Funcoes

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')


@bp_login.route ("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    # cria o objeto e armazena o usuario e senha digitado
    cliente = Clientes()
    funcoes = Funcoes()

    cliente.login = request.form['usuario'] 
    cliente.senha = funcoes.encrypt(request.form['senha'])

    # realiza a busca pelo usuario e armazena o resultado no objeto
    cliente.selectLogin()

    # verifica se usuario foi encontrado
    if cliente.id_cliente > 0:
        # limpa a sessão
        session.clear()
        # registra usuario na sessão, armazenando o login do usuário
        session['usuario'] = cliente.nome
        session['login'] = cliente.login
        session['grupo'] = cliente.grupo

        #log
        log = "Login Efetuado com sucesso" + "|Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        # abre a aplicação na tela home
        return redirect(url_for('home.home'))
    else:
        #log
        logUsuario = request.form['usuario']
        log = "Tentativa de Login" + "|Usuário:" + logUsuario + "|"
        funcoes.logWarning(log)

        # retorna para a tela de login
        return redirect(url_for('login.login', falhaLogin=1))

@bp_login.route ("/logout", methods=['POST'])
def logout():
    funcoes = Funcoes()
    #log
    log = "Logoff Efetuado" + "|Usuário:" + session['usuario'] + "|"
    funcoes.logInfo(log)

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