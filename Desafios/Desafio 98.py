print('-=' * 50)
print('''Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.''')
from time import sleep
print('-=' * 50)
def contador(i, f, p):
    if i > f:
        p *= (-1)
        f -= 1
    else:
        f += 1
    for c in range(i, f, p):
        sleep(0.3)
        print(c, end=" ")

print('Contando de 1 até 10 de 1 em 1!:')
contador(1, 10, 1)
print('\nContando de 10 até 0 de 2 em 2!:')
contador(0, 10, 2)
print('\nFaça sua contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: ')))



contador(i, f, p)