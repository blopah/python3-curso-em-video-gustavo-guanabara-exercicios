print("""Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.""")

import random
from time import sleep

bet = input('\nAdivinhe o número de 0 a 5: ')

res = str(random.randint(0, 5))

# if (type(bet)) != int:
#     bet = 6
print('Processando...')
sleep(1)

if bet == res:
    print('Congrats! {} is the right number!'.format(bet))
else:
    print("Assole! It's not {}! It's {}!".format(bet, res))