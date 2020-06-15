print('''Crie um programa que leia o nome e o preço de vários 
produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.''')

print('{:|^100}'.format('*Lista de compras*'))
keep = 'S'
tot = 0
mm = 0
li = []
b = ''
cont = 0
while True:
    pi = ki = True
    cont += 1
    print('{:|^100}'.format('*Produto Nº{}*'.format(cont)))
    nome = str(input('Insira o nome do produto: '))
    while pi:
        preco = input('Insira o preço do produto: R$')
        if preco.isnumeric():
            preco = float(preco)
            pi = False
    tot += preco
    if preco > 1000:
        mm += 1
    if cont == 1 or preco < li[0]:
        b = nome
    li.append(preco)
    li.sort()
    while ki:
        keep = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if keep in 'SsNn':
            ki = False
    if keep in 'Nn':
        break
print(f'Você gastou no total R${tot:.2f} nessa compra.')
print(f'{mm} produtos custam mais de mil reais.')
print(f'O produto mais barato foi a {b} que custa R${li[0]:.2f}')