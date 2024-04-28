import os;
from db import DataBase

class interface:

    def __init__(self):
        self.banco = DataBase ("DataBase.db ")

    def printLogo(self):
        print("=====================")
        print("Data Base Utilitario")
        print("=====================")

    def menu(self):
        print("1. Acesse o Banco de Dados ")
        print("2. cadastre um novo produto ")
        print("3. Atualize um produto ")
        print("4. Exclua um produto ")
        print("5. visualize ultimas notificações ")
        print("6. Sair ")

    def limparTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def selecionaOpcao(self, opcoes = []):
        opcaoSelecionada = input("Escolha sua opção ")

        if opcaoSelecionada == "": ## caso opcao seja preenchida vazia 
            return self.selecionaOpcao(opcoes)
        
        try:
            opcaoSelecionada == int(opcaoSelecionada)
        except ValueError:
            print("opcão invalida!!!")
            return self.selecionaOpcao(opcoes)
        
        return opcaoSelecionada
 
    def cadastroProduto(self):

        self.printLogo()

        print("Insira os dados do produto")
        print ("Campos com * são obrigatórios")

        nome = self.solicitaValor("Digite o nome do produto* ", 'texto', False)
        marca = self.solicitaValor("Digite a marca do prduto ", 'texto', False)
        qntd_caixas = self.solicitaValor("Digite a quantidade de caisa", 'numero', False)
        qntd_produto = self.solicitaValor("Digita a quantidade de produtos por caixa", 'numero', False)
        preco = self.solicitaValor("Digite o preco do prduto", 'numero', True)
        validade = self.solicitaValor ("Digite a data de validade do produto", 'numero', True)


        valores =  {
            "produto": nome,
            "marca": marca,
            "qntd_caixas": qntd_caixas,
            "qntd_produto": qntd_produto,
            "preco": preco,
            "validade": validade,
        }

        self.banco.inserir(valores)

        def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
            valor = input(legenda)

            if valor == "" and not permiteNulo:
                print("Valor inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            elif valor == "" and permiteNulo:
                return valor
            
            if tipo == 'numero':
                try:
                    valor = float(valor)
                except ValueError:
                    print("Valor inválido!")
                    return self.solicitaValor(legenda, tipo, permiteNulo)
            return valor
        
        def mostrarLista(self):
            pass