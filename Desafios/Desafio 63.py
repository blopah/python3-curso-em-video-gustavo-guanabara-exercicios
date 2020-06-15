print("""Escreva um programa que leia um número n inteiro 
qualquer e mostre na tela os n primeiros elementos de uma 
sequencia de Fibonacci.""")

n = int(input('Insira um número inteiro: '))
fibl = [0, 1]
for f in range(0, n, 1):
    soma = fibl[-2] + fibl[-1]
    fibl.append(soma)
# fibonacci = str(fibl)
print('Os {} primeiros elementos de Fibonacci são: \n{}...]'.format(n, fibl[:n]))
