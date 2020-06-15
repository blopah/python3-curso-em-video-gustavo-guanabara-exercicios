print('''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.''')

from random import randint
from time import sleep

li = []
num = int(input('Quantos jogos desejas fazer? '))
print('{:=^50}'.format(f'-Sorteando {num} jogos-'))
for c in range(0, num, 1):
    li.append([])
for co in range(0, num, 1):
    for con in range(0, 6, 1):
        while True:
            rn = randint(0, 60)
            if rn not in li[co]:
                break
        li[co].append(rn)
        li[co].sort()
    sleep(0.1)
    print(f'Jogo {co+1}: {li[co]}')
print('{:=^50}'.format(f'-Boa Sorte!-'))