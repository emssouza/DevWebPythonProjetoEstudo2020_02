#coding: utf-8

from flask import Flask
from mod_cliente.cliente import bp_cliente
from mod_erro.erro import bp_erro
from mod_home.home import bp_home
from mod_pedido.pedido import bp_pedido
from mod_produto.produto import bp_produto

app = Flask(__name__)

app.register_blueprint(bp_cliente)
app.register_blueprint(bp_erro)
app.register_blueprint(bp_home)
app.register_blueprint(bp_pedido)
app.register_blueprint(bp_produto)

@app.route("/resultado/",
methods=['GET','POST'])
def resultado():
    if request.method == "GET":
        auxNome = request.args.get('nome')
        auxIdade = request.args.get('idade')
    elif request.method == "POST":
        auxNome = request.form['nome']
        auxIdade = request.form['idade']
    return "Nome: {} <br>Idade: {}".format(auxNome,auxIdade), 200


if __name__ == '__main__':
    app.run()