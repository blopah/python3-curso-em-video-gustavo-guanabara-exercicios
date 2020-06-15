print("""Faça um programa que leia um ano qualquer e mostre se ele é bissexto.""")

ano = input('Digite um ano: ')
num = ano.isnumeric()
if num == True:
    ano = int(ano)
    bi = ano % 4
    if bi == 0:
        print('Este ano é bissexto.')
    else:
        print('Este ano não é bissexto')
else:
    print('Entrada invalida')