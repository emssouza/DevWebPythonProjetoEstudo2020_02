#coding: utf-8

from flask import Blueprint, render_template, request
from mod_login.login import validaSessao

bp_pedido = Blueprint('pedido', __name__,
                      url_prefix='/pedido', template_folder='templates')


@bp_pedido.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaPedidos():
    return render_template("formListaPedidos.html")


@bp_pedido.route("/formPedido", methods=['GET', 'POST'])
@validaSessao
def formPedido():
    return render_template("formPedido.html")
