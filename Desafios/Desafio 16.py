import math

print('\nCrie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira')

rnum = float(input('\nDigite um número Real: '))

inum = math.trunc(rnum)

print(inum)