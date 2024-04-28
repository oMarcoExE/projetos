from db import DataBase
from ui import interface

ui = interface()

opcao = ""
ui.limparTela
ui.printLogo
ui.menu
while opcao != 0:
    ui.limparTela
    ui.printLogo
    ui.menu
    opcao = ui.selecionaOpcao([1, 2, 3, 4 , 5 , 0])


    if opcao == 1:
        ui.cadastroProduto
        opcao = ""
