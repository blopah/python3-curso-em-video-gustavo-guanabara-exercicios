print('''Aprimore o Desafio 093 para que funcione com varios jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de 
cada jogador.
''')

#captação de dados.txt
jogador = dict()
time = list()
print('{:=^50}'.format(' Gerenciamento de Aproveitamento '))
while True:
    keep = '0'
    jogador['Nome'] = input('Nome: ')
    jogador['Partidas'] = int(input('Quantidade de partidas: '))
    jogador['Gols'] = list()
    for p in range(1, jogador['Partidas']+1):
        jogador['Gols'].append(int(input(f'Quantidade de gols na {p}º partida: ')))
    jogador['Gols totais'] = sum(jogador['Gols'])
    time.append(jogador.copy())
    while keep not in 'SsNn':
        keep = input('Deseja continuar? [S/N] ').upper()[0]
    if keep in 'Nn':
        break
#print de tudo
print('{:=^50}'.format('Dados do Time'))
print('{: ^15}'.format('Codigo'), end='')
print('{: ^15}'.format('Nome'), end='')
print('{: ^15}'.format('Partidas'), end='')
print('{: ^15}'.format('Gols'), end='')
print('{: ^15}'.format('Gols Totais'))
contador = 0
for p in time:
    contador += 1
    print('{: ^15}'.format(contador), end='')
    print('{: ^15}'.format(p['Nome']), end='')
    print('{: ^15}'.format(p['Partidas']), end='')
    print('{: ^15}'.format(str(p['Gols'])), end='')
    print('{: ^15}'.format(p['Gols totais']))
#analise de dados.txt
while True:
    select = int(input('Mostrar dados.txt de qual jogador? (999 para parar)'))
    if select == 999:
        break
    while select > len(time):
        select = int(input('Mostrar dados.txt de qual jogador? (999 para parar)'))
    print('{:=^50}'.format(f'Levantamento do jogador {time[select-1]["Nome"]} '))
    print(f'O jogador {time[select-1]["Nome"]} jogou {time[select-1]["Partidas"]} jogos e fez {str(time[select-1]["Gols totais"])} gols no total.')
    for contador in range(0, len(time[select-1]["Gols"])):
        print(f'No {contador+1}º jogo fez {time[select-1]["Gols"][contador]} gols')
# print(jogador)