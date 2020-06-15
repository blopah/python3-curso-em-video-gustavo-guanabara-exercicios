print("""\033[1;30mCrie um programa que leia vários números inteiros 
pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles. 
(desconsiderando o flag)\033[0;0m""")

a = 0
soma = 0
cont = -1
while a != 999:
    soma += a
    cont += 1
    a = int(input('Digite um número para ser somado ou "999" para encerrar: '))
print('A soma dos {} números digitados é {}.'.format(cont, soma))
