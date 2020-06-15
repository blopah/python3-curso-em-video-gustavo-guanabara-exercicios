print('''Aprimore o desafio anterior mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.''')

li = [[],[],[]]

for c in range(0, 3, 1):
    for co in range(0, 3, 1):
        li[c].append(int(input(f'Insira um valor para a posição [{c}],[{co}]: ')))
print('{:=^40}'.format(''))
print(f'''[ {li[0][0]} ][ {li[0][1]} ][ {li[0][2]} ]
[ {li[1][0]} ][ {li[1][1]} ][ {li[1][2]} ]
[ {li[2][0]} ][ {li[2][1]} ][ {li[2][2]} ]''')

somapar = 0
somater = 0
maiseg = li[1][0]
for c in range(0, 3, 1):
    for co in range(0, 3, 1):
        if li[c][co] % 2 == 0:
            somapar += li[c][co]

for c in range(0, 3, 1):
    somater += li[2][c]

for c in range(0, 3, 1):
    if li[1][c] > maiseg:
        maiseg = li[1][c]

print(f'a) A soma de todos os valores pares digitados é {somapar}')
print(f'b) A soma dos valores da terceira coluna é {somater}')
print(f'c) O maior valor da segunda linha é {maiseg}')