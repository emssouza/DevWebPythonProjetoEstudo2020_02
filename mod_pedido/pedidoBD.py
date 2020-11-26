from flask import session
from BancoBD import Banco
from funcoes import Funcoes

class Pedidos(object):
    def __init__(self, id_pedido=0, data_hora="", id_cliente=0, observacao=""):
        self.id_pedido = id_pedido
        self.data_hora = data_hora
        self.id_cliente = id_cliente
        self.observacao = observacao

    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select tbp.id_pedido, tbp.data_hora, tbc.nome, tbp.observacao from tb_pedidos tbp inner join tb_clientes tbc on tbp.id_cliente = tbc.id_cliente"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            return "Ocorreu um erro na busca do pedido"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectONE(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_pedido, data_hora, id_cliente, observacao from tb_pedidos where id_pedido = %s"
            _sql_data = (self.id_pedido,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_pedido = linha[0]
                self.data_hora= linha[1]
                self.id_cliente = linha[2]
                self.observacao = linha[3]
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do pedido"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insert(self):
        banco = None
        c = None
        funcoes = Funcoes()
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "insert into tb_pedidos(data_hora, id_cliente, observacao) values (%s,%s,%s)"
            _sql_data = (self.data_hora, self.id_cliente, self.observacao,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Pedido cadastrado com sucesso!"
        except Exception as e:
            raise Exception('Erro ao tentar cadastrar pedido!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def update(self):
        banco = None
        c = None
        funcoes = Funcoes()
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "update tb_pedidos set data_hora=%s,id_cliente=%s,observacao=%s where id_pedido = %s"
            _sql_data = (self.data_hora, self.id_cliente, self.observacao, self.id_pedido,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()

            return "Pedido atualizado com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar pedido!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "delete from tb_pedidos where id_pedido = %s"
            _sql_data = (self.id_pedido,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Pedido excluído com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir pedido!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


class ProdutoPedidos(object):
    def __init__(self, id_pedido=0, id_produto=0, quantidade=0, valor=0, observacao=""):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.valor = valor
        self.observacao = observacao

    def selectALLProdutoPedido(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select pp.id_pedido, pp.id_produto, pp.quantidade, pp.valor, pp.observacao, CONVERT(p.imagem USING utf8) from tb_pedido_produtos pp inner join tb_produtos p on pp.id_produto= p.id_produto"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            return "Ocorreu um erro na busca do pedido"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectONEProdutoPedido(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_pedido, id_produto, quantidade, valor, observacao from tb_pedido_produtos where id_pedido = %s"
            _sql_data = (self.id_pedido,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_pedido = linha[0]
                self.id_produto= linha[1]
                self.quantidade= linha[2]
                self.valor= linha[3]
                self.observacao = linha[4]
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do pedido"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insertProdutoPedido(self):
        banco = None
        c = None
        funcoes = Funcoes()
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "insert into tb_pedido_produtos(id_pedido, id_produto, quantidade, valor, observacao) values (%s,%s,%s,%s,%s)"
            _sql_data = (self.id_pedido, self.id_produto, self.quantidade, self.valor, self.observacao)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Produto cadastrado com sucesso!"
        except Exception as e:
            raise Exception('Erro ao tentar cadastrar produto!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def updateProdutoPedido(self):
        banco = None
        c = None
        funcoes = Funcoes()
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "update tb_pedido_produtos set quantidade, valor,observacao=%s where id_produto = %s and id_pedido =%s"
            _sql_data = (self.quantidade, self.valor, self.observacao, self.id_produto, self.id_pedido,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()

            return "Pedido atualizado com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar pedido!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def deleteProdutoPedido(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "delete from tb_pedido_produtos where id_produto = %s and id_pedido =%s"
            _sql_data = (self.id_produto,self.id_pedido,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Produto excluído com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()