print('''Faça um programa que tenha uma função chamada maior(), que 
recebe vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é maior.''')

from time import sleep

def maior(* p):
    m = max(p)
    print('-=' * 30)
    sleep(1)
    print('Analisando os dados.txt...')
    sleep(1)
    print(f'Os dados.txt são {p}.')
    sleep(1)
    print(f'O maior é {m}.')
    sleep(1)


maior(8, 89, 56, 21, 45)
maior(84, 87, 65, 2, 0, 84, 56, 100, 105)