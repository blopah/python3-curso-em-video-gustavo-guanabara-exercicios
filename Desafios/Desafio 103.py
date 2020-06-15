print('''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
O nome de um jogador
Quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.''')

def ficha(n='', g=''):
    if n == '':
        n = '<Desconhecido>'
    if g == '':
        g = '<Desconhecido>'
    print(f'O jogador {n} fez {g} gols no campeonato.')

nome = input('Nome do Jogador: ')
gols = input('Gols marcados: ')

ficha(nome, gols)