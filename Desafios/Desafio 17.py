print('\nFaça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, \ncalcule e mostre o comprimento da hipotenusa.')

import math

cato = float(input('Digite o tamanho do cateto oposto em "cm": '))
cata = float(input('Digite o tamanho do cateto adjacente em "cm": '))

catopow = pow(cato, 2)
catapow = pow(cata, 2)

scatocata = (catopow+catapow)

h = math.sqrt(scatocata)

print('A hipotenusa é igual a {:.2f}.'.format(h))