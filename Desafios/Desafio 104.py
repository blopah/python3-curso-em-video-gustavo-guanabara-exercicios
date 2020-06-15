print('''Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.''')
def leiaint(txt):
    print(txt, end='')
    e = input()
    ok = e.isnumeric()
    while not ok:
        print(f'\033[1;31mO charactere {e} não é um número inteiro!')
        e = input('\033[1;30mDigite um número')
        ok = e.isnumeric()
    print(f'\033[1;30mO charactere {e} é um número inteiro!')

e = leiaint('\033[1;30mDigite um número: ')