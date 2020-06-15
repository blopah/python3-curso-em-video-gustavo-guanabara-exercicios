print('''Faça um programa que jogue par ou impar com o computador. 
O jogo só será interrompido quando o jogador PERDER, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.''')
from time import sleep
from random import randint
c = 0
while True:
    comp = int(randint(0, 10))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    jog = int(input('insira um número: '))
    soma = int(comp + jog)
    if (soma % 2) == 0:
        win = 'P'
        res = 'PAR'
    else:
        win = 'I'
        res = 'IMPAR'
    if win == pi:
        print(f'Você jogou {jog}, o computador jogou {comp}. Deu {soma} que é {res}.')
        print('{:-^100}'.format('Você ganhou!'))
        c += 1
    else:
        print(f'Você jogou {jog}, o computador jogou {comp}. Deu {soma} que é {res}.')
        print('{:-^100}'.format(f'Você perdeu! Conseguiu ganhar \033[1;31m{c}x\033[0;0m seguidas!'), end=' ')
        break
# print(f'Conseguiu ganhar {c}x seguidas!')








