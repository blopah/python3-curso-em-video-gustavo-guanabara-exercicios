print('''Crie um programa que tenha uma tupla única com nomes 
de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando 
os dados.txt em forma tabular.''')

print(f'{" Cadastre 10 produtos com nome e preço ":=^41}')
li = []
for c in range(0, 3, 1):
    nome = str(input('Insira o nome do produto: ')).strip().capitalize()
    preço = float(input(f'Insira o preço do {nome}: R$'))
    li.append(nome)
    li.append(preço)
print(f'{"":=^41}')
print(f'{" Lista de produtos cadastrados ":=^41}')
print(f'{"":=^41}')
for produtos in range(0, len(li), 2):
    print(f'{li[produtos]:.<31}', end='R$')
    print(f'{li[produtos + 1]: >10.2f}')
print(f'{" FIM ":=^41}')
print(li)
