import math

print('\nFaça um programa que leia um ângulo qualquer e mostre na tela o valor do \nseno, cosseno e tangente desse ângulo.')

num = float(input('Digite um ângulo qualquer: '))

numc = math.radians(num)

sen = math.sin(numc)
cos = math.cos(numc)
tan = math.tan(numc)


print('O seno de {} é: {:.2f} \nO cosseno de {} é: {:.2f} \nA tangente de {} é: {:.2f}'.format(num, sen, num, cos, num, tan))
