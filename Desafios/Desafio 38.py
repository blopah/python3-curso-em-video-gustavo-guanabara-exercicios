print("""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
• O primeiro valor é maior. ou
• O segundo valor é maior. ou
• Não existe valor maior, os dois valores são iguais.""")

num1 = int(input('Insira um valor inteiro: '))
num2 = int(input('Insira outro valor inteiro: '))

if num1 > num2:
    print('O primeiro valor({}) é maior'.format(num1))
elif num2 > num1:
    print('O segundo valor({}) é maior'.format(num2))
else:
    print('Não existe valor maior, os dois valores({} e {}) são iguais.'.format(num1, num2))