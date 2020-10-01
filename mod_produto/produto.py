#coding: utf-8

from flask import Blueprint, render_template, request
from mod_login.login import validaSessao

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')


@bp_produto.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaProdutos():
    return render_template("formListaProdutos.html")


@bp_produto.route("/formProduto", methods=['GET', 'POST'])
@validaSessao
def formProduto():
    return render_template("formProduto.html")
