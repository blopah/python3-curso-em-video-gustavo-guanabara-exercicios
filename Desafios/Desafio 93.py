print('''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo 
o total de gols feitos durante o campeonato.''')

jogador = dict()
print('{:=^50}'.format(' Gerenciamento de Aproveitamento '))
jogador['Nome'] = input('Nome: ')
jogador['Partidas'] = int(input('Quantidade de partidas: '))
jogador['Gols'] = list()
for p in range(1, jogador['Partidas']+1):
    jogador['Gols'].append(int(input(f'Quantidade de gols na {p}º partida: ')))
jogador['Gols totais'] = sum(jogador['Gols'])

for k, v in jogador.items():
    print(f'{k}: {v}')
print(jogador)