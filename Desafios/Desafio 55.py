print("""Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.""")
me = 0
ma = 0
for c in range(1, 5, 1):
    a = float(input('Insira o peso em Kg: '))
    if c == 1:
        me = a
        ma = a
    else:
        if a > ma:
            ma = a
        if a < me:
            me = a

print('O maior peso é {}Kg, e o menor peso é {}Kg.'.format(ma, me))