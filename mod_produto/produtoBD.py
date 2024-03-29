from flask import session
from BancoBD import Banco
from funcoes import Funcoes

class Produtos(object):
    def __init__(self, id_produto=0, descricao="", valor=0, imagem=""):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor
        self.imagem = imagem

    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_produto, descricao, valor, CONVERT(imagem USING utf8) from tb_produtos"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            return "Ocorreu um erro na busca do produto"
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
            _sql = "select id_produto, descricao, valor, CONVERT(imagem USING utf8) from tb_produtos where id_produto = %s"
            _sql_data = (self.id_produto,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_produto = linha[0]
                self.descricao = linha[1]
                self.valor = linha[2]
                self.imagem = linha[3]
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
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
            print(self.imagem)
            c = banco.conexao.cursor()
            _sql = "insert into tb_produtos(descricao, valor, imagem) values (%s,%s,%s)"
            _sql_data = (self.descricao, self.valor, self.imagem,)
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

    def update(self):
        banco = None
        c = None
        try:
            banco = Banco()
            print(self.imagem)
            c = banco.conexao.cursor()
            _sql = "update tb_produtos set descricao=%s,valor=%s,imagem=%s where id_produto = %s"
            _sql_data = (self.descricao, self.valor, self.imagem, self.id_produto,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()

            return "Produto atualizado com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar produto!", str(e))
        
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
            _sql = "delete from tb_produtos where id_produto = %s"
            _sql_data = (self.id_produto,)
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