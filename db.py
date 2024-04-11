import sqlite3 

class DataBase:
    def __init__ (self, banco_dados):
        self.concertarBanco(banco_dados)

    def conconcertarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)



    