print("""Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo""")

n = int(input('Insira um número inteiro: '))
d = 0
for c in range(1, n, 1):
    if (n % c) == 0:
        d += 1
    # print(d)
if d > 1:
    print('{} Não é um número primo.'.format(n))
else:
    print('{} É um número primo.'.format(n))
