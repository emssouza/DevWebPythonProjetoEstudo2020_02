#coding: utf-8

from flask import Blueprint, render_template, request
from mod_login.login import validaSessao

bp_cliente = Blueprint('cliente', __name__,
                       url_prefix='/cliente', template_folder='templates')


@bp_cliente.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaClientes():
    return render_template("formListaClientes.html")


@bp_cliente.route("/formCliente", methods=['GET', 'POST'])
@validaSessao
def formCliente():
    return render_template("formCliente.html")
