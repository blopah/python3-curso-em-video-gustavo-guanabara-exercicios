print("""Crie um programa que leia o ano de nascimento de 
sete pessoas. No final, mostre quantas pessoas ainda não 
atingiram a maioridade e quantas já são maiores.""")
import datetime
now = datetime.datetime.now().year
ma = 0
me = 0
for c in range(0, 7, 1):
    bd = int(input('Insira o ano de nascimento: '))
    if (now - bd) > 21:
        ma += 1
    else:
        me += 1
print('{} são maiores de idade, e {} são menores de idade'.format(ma, me))