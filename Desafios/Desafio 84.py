print('''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.''')

p = list()
ps = list()
pl = list()
pp = list()
while True:
    keep = '0'
    p.append(input('Nome: ').strip().capitalize())
    p.append(int(input('Peso: Kg')))
    ps.append(p[:])
    p.clear()
    print(p)
    print(ps)
    while keep not in 'SsNn':
        keep = input('Deseja continuar?').strip().capitalize()
    if keep in 'Nn':
        break
print(f'{len(ps)} pessoas foram cadastradas.')
for pessoa in enumerate(ps):
    no = 1
    if pessoa[0] == 0:
        pl.append(pessoa[1])
    else:
        for c in range(0, len(pl), 1):
            if pessoa[len(pessoa)-1][1] < pl[c][1]:
                pl.insert(c, pessoa[len(pessoa) - 1])
                no = 0
                break
        if no == 1:
            pl.append(pessoa[len(pessoa) - 1])
pp = pl[:]
pp.reverse()
print(f'Todas as pessoas são: {ps}')
print(f'As pessoas mais leves são: {pl}')
print(f'As pessoas mais pesadas são: {pp}')
