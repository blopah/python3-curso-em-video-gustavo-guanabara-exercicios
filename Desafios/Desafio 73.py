print('''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense''')

time = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético', 'Goiás', 'Botafogo', 'Bahia', 'São', 'Paulo', 'Corinthians', 'Grêmio', 'Athletico-PR', 'Ceará', 'SC', 'Fortaleza', 'Vasco da Gama', 'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
print(f'\n\033[1;31mOs 5 primeiros colocados são: \033[0;0m')
for cinco in range(0, 5, 1):
    print(time[cinco], end=', ')
print('\n\033[1;31mOs 4 últimos colocados da tabela são: \033[0;0m')
for cinco in range((len(time)-4), len(time), 1):
    print(time[cinco], end=', ')
print('\n\033[1;31mOs times por ordem alfabética são: \033[0;0m')
for cinco in range(0, len(time), 1):
    print(sorted(time)[cinco], end=', ')
print(f'\n\033[1;31mO Chapecoense está na {(time.index("Chapecoense")-1)}ª posição da tabela\033[0;0m')