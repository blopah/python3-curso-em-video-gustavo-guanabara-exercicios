print('''\033[4;30mMelhore o jogo do Desafio 28 onde o computador vai "pensar" 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar 
acertar, mostrando no final quantos palpites foram necessários para
vencer.\033[m''')

import random
from time import sleep

rep = True
cont = 0
bet = int(input('\nBet a number between 0 and 10: '))
res = int(random.randint(0, 10))
res = int(5)
while rep == True:
    cont += 1
    print('Processing...')
    sleep(0)

    if bet == res:
        print('Congrats! {} is the right number!'.format(bet))
        print("You've gone {} attempts to get it!".format(cont))
        rep = False
    else:
        if bet > res:
            print("Assole! It's not {}! It's less!".format(bet, res))
            bet = int(input('\nTry again a number between 0 and 10: '))
        else:
            print("Assole! It's not {}! It's more!".format(bet, res))
            bet = int(input('\nTry again a number between 0 and 10: '))