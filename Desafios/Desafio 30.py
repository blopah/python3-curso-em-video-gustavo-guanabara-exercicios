print("""Crie um programa que leia um número inteiro e mostre na tela se ele é 'par' ou 'ímpar'.""")

nume = input('Digite qualquer número inteiro: ')
if nume.isnumeric():
    num = int(nume)
    if num % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
else:
    print('Entrada inválida.')
