#coding: utf-8

from flask import Blueprint, render_template, request

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/", methods=['GET', 'POST'])
def formListaClientes():
    return render_template("formListaClientes.html")

@bp_cliente.route("/formCliente", methods=['POST'])
def formCliente():
    return render_template("formCliente.html")