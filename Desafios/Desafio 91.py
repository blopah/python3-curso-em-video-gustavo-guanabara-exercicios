print('''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número dado.''')

from random import randint
from operator import itemgetter
players = dict()
ranking = list()
for c in range(1, 5, 1):
    n1 = randint(1, 6)
    players[f'Jogador {c}'] = n1
for k, v in players.items():
    print(f'O {k} fez {v} pontos.')
print()
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('{:-^35}'.format(' - Ranking - '))
for r in enumerate(ranking):
    print(f'Em {r[0]+1}º lugar o {r[1][0]} com {r[1][1]} pontos!')