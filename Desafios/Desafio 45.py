print('\033[1;31m{:=^130}\n{:=^147}\n{:=^130}'.format('','\033[1;34;40mJO KEN PO!\033[1;31m',''))
import random
import time

jogador = str(input('\033[1;30mPedra, papel ou tesoura?\033[0;0m ')).title().strip()
print('Você escolheu {}!'.format(jogador))
computador = random.randint(1, 3)
time.sleep(1)
print('\033[1;31mJO')
time.sleep(1)
print('\033[1;34mKEN')
time.sleep(1)
print('\033[1;33mPO!')
opcoes = ['nada', 'Pedra', 'Papel', 'Tesoura']
if jogador == opcoes[computador]:
    print('Empate!\033[0;0m')
elif jogador == 'Pedra':
    if computador == 2:
        print('\033[1;31mVOCE PERDEU!\033[0;0m')
    else:
        print('\033[1;34mVOCE GANHOU!\033[0;0m')
elif jogador == 'Papel':
    if computador == 3:
        print('\033[1;31mVOCE PERDEU!\033[0;0m')
    else:
        print('\033[1;34mVOCE GANHOU!\033[0;0m')
elif jogador == 'Tesoura':
    if computador == 1:
        print('\033[1;31mVOCE PERDEU!\033[0;0m')
    else:
        print('\033[1;34mVOCE GANHOU!\033[0;0m')
else:
    print('Jogada invalida. Tente novamente!')
print('O computador escolheu {}!'.format(opcoes[computador]))