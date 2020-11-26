#coding: utf-8

from flask import Blueprint, render_template, request, jsonify, session
import base64
from mod_login.login import validaSessao
from mod_produto.produtoBD import Produtos
from funcoes import Funcoes

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')


@bp_produto.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaProdutos():
    produto = Produtos()
    res = produto.selectALL()
    return render_template('formListaProdutos.html', result=res, content_type='application/json')

@bp_produto.route("/formProduto", methods=['POST'])
@validaSessao
def formProduto():
    produto = Produtos()
    return render_template('formProduto.html', produto=produto, content_type='application/json')

@bp_produto.route('/formEditProduto', methods=['POST'])
@validaSessao
def formEditProduto():
    produto = Produtos()
    produto.id_produto = request.form['id_produto']
    produto.selectONE()
    return render_template('formProduto.html', produto=produto, content_type='application/json')

@bp_produto.route('/addProduto', methods=['POST'])
@validaSessao
def addProduto():
    _msg = ""
    produto = Produtos()
    funcoes = Funcoes()
    try:
        produto.id_produto = request.form['id_produto']
        produto.descricao = request.form['descricao']
        produto.valor = request.form['valor']
        produto.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode(request.files['imagem'].read()), "utf-8")
        
        _msg = produto.insert()

        #log
        log = _msg + "| Produto: " + request.form['descricao']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = "Erro ao Adicionar Produto: " + _msg + "| Produto: " + request.form['descricao'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_produto.route('/editProduto', methods=['POST'])
@validaSessao
def editProduto():
    _msg = ""
    funcoes = Funcoes()
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.descricao = request.form['descricao']
        produto.valor = request.form['valor']
        produto.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str (base64.b64encode(request.files['imagem'].read()), "utf-8")

        _msg = produto.update()

        #log
        log = _msg + "| Produto: " + request.form['id_produto']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Produto: " + request.form['id_produto'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_produto.route('/deleteProduto', methods=['POST'])
@validaSessao
def deleteProduto():
    funcoes = Funcoes()
    _msg = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        _msg = produto.delete()

        #log
        log = _msg + "| Produto: " + request.form['id_produto']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Produto: " + request.form['id_produto'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)