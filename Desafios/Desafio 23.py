print("""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.""")

num = input('digite um número de 4 dígitos: ')

nume = num[:4]
u = num[3]
d = num[2]
c = num[1]
m = num[0]

print('O número é {}. \nUnidade {}. \nDezena {}. \nCentena {}. \nMilhar {}.'.format(nume, u, d, c, m))