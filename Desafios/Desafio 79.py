print('''
Crie um programa onde o usuário possa digitar 
vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos, em ordem crescente.''')

li = []
while True:
    keep = ' '
    valor = input('Digite um valor: ')
    if valor in li:
        print('Este valor já esta na lista.')
    else:
        li.append(valor)
    while keep not in 'SsNn':
        keep = input('Deseja continua? [S/N] ')
        if keep not in 'SsNn':
            print('Opção inválida')
    if keep in 'Nn':
        break
li.sort()
print(li)