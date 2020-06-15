print("""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.""")

pt = int(input('Insira o primeiro termo PA: '))
r = int(input('Insira A razão da PA: '))
print('Os 10 primeiros termos desta PA são: (', end='')
for c in range(pt, (10*r), r):
    print('{}, '.format(c), end='')
print('...)')