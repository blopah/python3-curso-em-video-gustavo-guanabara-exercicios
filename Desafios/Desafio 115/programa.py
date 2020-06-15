from funcoes import *

opc = ['CONSULTAR', 'CADASTRAR', 'SAIR']

criaarq()

while True:
    mostra_menu(opc)
    ordem = recebe_ordem(opc)
    if ordem == 2:
        titulo('SAINDO...')
        break
    executar(ordem)