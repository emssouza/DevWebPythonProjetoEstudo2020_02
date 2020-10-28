import pymysql

class Banco():
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "Ems.1422"
        db = "db_abc_bolinhas"
        self.conexao = pymysql.connect(host, user, password, db)