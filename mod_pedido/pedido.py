#coding: utf-8

from flask import Blueprint, render_template, request, jsonify, session
import base64
from mod_login.login import validaSessao
from mod_pedido.pedidoBD import Pedidos
from mod_pedido.pedidoBD import ProdutoPedidos
from mod_cliente.clienteBD import Clientes
from mod_produto.produto import Produtos
from funcoes import Funcoes


bp_pedido = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates')


@bp_pedido.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaPedidos():
    pedido = Pedidos()
    res = pedido.selectALL()
    return render_template('formListaPedidos.html', result=res, content_type='application/json')

@bp_pedido.route("/formPedido", methods=['POST'])
@validaSessao
def formPedido():
    pedido = Pedidos()
    cliente = Clientes()
    listaClientes = cliente.selectALL()
    return render_template('formPedido.html', pedido=pedido, listaClientes=listaClientes, content_type='application/json')

@bp_pedido.route('/formEditPedido', methods=['POST'])
@validaSessao
def formEditPedido():
    cliente = Clientes()
    listaClientes = cliente.selectALL()
    pedido = Pedidos()
    pedido.id_pedido = request.form['id_pedido']
    pedido.selectONE()
    return render_template('formPedido.html', pedido=pedido, listaClientes=listaClientes, content_type='application/json')


@bp_pedido.route('/addPedido', methods=['POST'])
@validaSessao
def addPedido():
    _msg = ""
    pedido = Pedidos()
    funcoes = Funcoes()
    try:
        pedido.id_pedido = request.form['id_pedido']
        pedido.data_hora = request.form['data_hora']
        pedido.id_cliente= request.form['id_cliente']
        pedido.observacao = request.form['observacao']
        
        _msg = pedido.insert()

        #log
        log = _msg + "| Cliente: " + request.form['id_cliente']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = "Erro ao Adicionar Pedido: " + _msg + "| Cliente: " + request.form['id_cliente'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_pedido.route('/editPedido', methods=['POST'])
@validaSessao
def editPedido():
    _msg = ""
    funcoes = Funcoes()
    try:
        pedido = Pedidos()
        pedido.id_pedido = request.form['id_pedido']
        pedido.data_hora = request.form['data_hora']
        pedido.id_cliente = request.form['id_cliente']
        pedido.observacao = request.form['observacao']

        _msg = pedido.update()

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_pedido.route('/deletePedido', methods=['POST'])
@validaSessao
def deletePedido():
    _msg = ""
    funcoes = Funcoes()
    try:
        pedido= Pedidos()
        pedido.id_pedido= request.form['id_pedido']
        _msg = pedido.delete()

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_pedido.route("/formListaProdutos", methods=['GET', 'POST'])
@validaSessao
def formListaProdutos():
    pedido = ProdutoPedidos()
    pedido.id_pedido = request.form['id_pedido']
    res = pedido.selectALLProdutoPedido()
    return render_template('formListaProduto.html', result=res, pedido=pedido, content_type='application/json')

@bp_pedido.route("/formAddProduto", methods=['POST'])
@validaSessao
def formAddProduto():
    pedido = ProdutoPedidos()
    produto = Produtos()
    listaProdutos = produto.selectALL()
    return render_template('formAddPedidoProduto.html', pedido=pedido, listaProdutos=listaProdutos, content_type='application/json')

@bp_pedido.route('/formEditProduto', methods=['POST'])
@validaSessao
def formEditProduto():
    produto = Produtos()
    listaProdutos = produto.selectALL()
    pedido = ProdutoPedidos()
    pedido.id_pedido = request.form['id_pedido']
    pedido.id_produto = request.form['id_produto']
    pedido.selectONEProdutoPedido()
    return render_template('formAddPedidoProduto.html', pedido=pedido, listaProdutos=listaProdutos, content_type='application/json')


@bp_pedido.route('/addProduto', methods=['POST'])
@validaSessao
def addProduto():
    _msg = ""
    pedido = ProdutoPedidos()
    funcoes = Funcoes()
    try:
        pedido.id_pedido = request.form['id_pedido']
        pedido.id_produto= request.form['id_produto']
        pedido.quantidade= request.form['quantidade']
        pedido.valor = request.form['valor']
        pedido.observacao = request.form['observacao']
        
        _msg = pedido.insertProdutoPedido()

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = "Erro ao Adicionar Pedido: " + _msg + "| Pedido: " + request.form['id_pedido'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_pedido.route('/editProduto', methods=['POST'])
@validaSessao
def editProduto():
    _msg = ""
    funcoes = Funcoes()
    try:
        pedido = ProdutoPedidos()
        pedido.id_pedido = request.form['id_pedido']
        pedido.id_produto= request.form['id_produto']
        pedido.quantidade= request.form['quantidade']
        pedido.valor = request.form['valor']
        pedido.observacao = request.form['observacao']

        _msg = pedido.updateProdutoPedido()

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_pedido.route('/deleteProduto', methods=['POST'])
@validaSessao
def deleteProduto():
    _msg = ""
    funcoes = Funcoes()
    try:
        pedido= ProdutoPedidos()
        pedido.id_pedido= request.form['id_pedido']
        pedido.id_produto= request.form['id_produto']
        _msg = pedido.deleteProdutoPedido()

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido']+ " |Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg + "| Pedido: " + request.form['id_pedido'] + " |Usuário:" + session['usuario']+ "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)