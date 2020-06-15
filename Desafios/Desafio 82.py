print('''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas 
os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.''')

li = []
while True:
    keep = 'a'
    num = int(input('Digite um número: '))
    li.append(num)
    while keep not in 'SsNn':
        keep = input('Deseja continuar?').strip()[0]
        if keep not in 'SsNn':
            print('Opção inválida.', end=' ')
    if keep in 'Nn':
        break
lip = []
lii = []
for n in li:
    if n % 2 == 0:
        lip.append(n)
    else:
        lii.append(n)
print(li)
print(lip)
print(lii)