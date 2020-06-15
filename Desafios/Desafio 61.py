print("""Refaça o Desafio 51 usando while.""")

print("""Exercício 51: 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.""")

pt = int(input('Insira o primeiro termo PA: '))
r = int(input('Insira A razão da PA: '))
c = 0
res = pt - r
prin = ''
while c < 10:
    res = res + r
    prin += str(res) + ', '
    c += 1
print('Os primeiros 10 termos desta PA são: ({}...)'.format(prin))