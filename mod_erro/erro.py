#coding: utf-8

from flask import Blueprint, render_template, request

bp_erro = Blueprint('erro', __name__, url_prefix='/erro', template_folder='templates')

@bp_erro.route(404)
def erro404(error):
    return render_template("form404.html")

@bp_cliente.route(500)
def erro500(error):
    return render_template("form500.html")