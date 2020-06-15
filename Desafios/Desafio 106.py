print('''Faça um mini sistema que utilize o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM",
o programa se encerrará. OBS:Use cores''')
from time import sleep

def msgr(x):
    l = len(x)+2
    print('\033[1;30;41m~' * l)
    print(f' {x}', end='')
    txt = input('')
    print('~' * l)
    return txt

def msgy(x):
    l = len(x)+2
    print('\033[1;30;43m~' * l)
    print(f' {x}')
    print('~' * l)
    print('\033[1;30;45m', end='')

def msgp(x):
    l = len(x)+2
    print('\033[1;30;45m~' * l)
    print(f' {x}')
    print('~' * l)


def ajuda():
    while True:
        txt = msgr('Função ou Biblioteca (FIM para sair)>')
        if txt in 'FIMfim':
            break
        sleep(1)
        msgy(f'Acessando a ajuda de {txt}.')
        sleep(1)
        help(txt)

ajuda()