#coding: utf-8

from flask import Blueprint, render_template, request

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/", methods=['POST'])
def formListaProdutos():
    return render_template("formListaProdutos.html")

@bp_produto.route("/formProduto", methods=['POST'])
def formProduto():
    return render_template("formProduto.html")