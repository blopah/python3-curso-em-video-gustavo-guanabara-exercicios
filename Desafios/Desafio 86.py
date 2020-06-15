print('''Crie um programa que crie uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado.
# 
No final, mostre a matriz na tela, com a formatação correta''')

li = [[],[],[]]

for c in range(0, 3, 1):
    li[0].append(input(f'Insira para a posição [0,{c}]: '))
for c in range(0, 3, 1):
    li[1].append(input(f'Insira para a posição [1,{c}]: '))
for c in range(0, 3, 1):
    li[2].append(input(f'Insira para a posição [2,{c}]: '))

print(f'''[ {li[0][0]} ][ {li[0][1]} ][ {li[0][2]} ]
[ {li[1][0]} ][ {li[1][1]} ][ {li[1][2]} ]
[ {li[2][0]} ][ {li[2][1]} ][ {li[2][2]} ]''')