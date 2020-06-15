print('''Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números
e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre 
todos os valores Pares sorteados pela função anterior.''')

from random import randint
from time import sleep

def sorteio(x):
    print('Os números sorteados são... ', end="")
    for c in range(0, 5, 1):
        sleep(0.5)
        n = randint(1, 30)
        x.append(n)
        print(f'{n} ', end='')
    print()

def soma(x, y):
    for i in x:
        if i % 2 == 0:
            y.append(i)

somapar = list()
numeros = list()
sorteio(numeros)
soma(numeros, somapar)
sleep(0.5)
print(f'Analisando os números.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print(f'Os números pares são... ', end='')
sleep(0.5)
print(f'{somapar}')
print(f'E a soma deles é... ', end='')
sleep(0.5)
print(f'{sum(somapar)}')