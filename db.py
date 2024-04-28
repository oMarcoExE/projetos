import sqlite3 

class DataBase:
    def __init__ (self, banco_dados):
        self.conconcertarBanco(banco_dados)

    def conconcertarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarBaseDeDados()

    def criarBaseDeDados(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS BaseDados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                marca TEXT NOT NULL,
                qntd_caixas TEXT NOT NULL,
                qntd_produto TEXT NOT NULL,
                preco TEXT NULL,
                validade date NOT NULL
            )
        """)
    
    def inserir(self, dados, valores):
        colunas = ', '.join(valores.keys())
        placeholders = ', '.join('?' * len(valores))

        sql = 'INSERT INTO BaseDados ({}) VALUES ({})'.format(colunas, placeholders)

        self.cursor.execute(sql, list(valores.values()))
        self.banco.commit()

        if self.cursor.lastrowid:
            print(f"{dados} produto salvo na base de dados!")
            return True
        else:
            print("Erro ao salvar produto!")
            return False
        
    def buscarDados(self, tabela, campos = '*'):
        sql = f"SELECT {campos} from {dados}"
        self.cursor.execute(sql)

        dados = self.cursor.fetchall()
        return dados


    