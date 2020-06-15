print('''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descrescente.
C) Se o valor 5 foi digitado e está ou não na lista.''')

num = cont = 0
li = []
while True:
    no = 1
    keep = 'a'
    cont += 1
    num = int(input('Digite um número: '))
    if cont == 1:
        li.append(num)
    else:
        for n in enumerate(li):
            if num <= li[n[0]]:
                li.insert(n[0], num)
                no = 0
                break
        if no == 1:
            li.append(num)
    while keep not in 'SsNn':
        keep = input('Deseja continuar? [S/N]')
        if keep not in 'SsNn':
            print('Opção inválida.', end=' ')
    if keep in 'Nn':
        break
print(f'Você digitou {len(li)} números.')
li.sort(reverse=True)
print(f'A lista de valores ordenada de forma descrescente é {li}')
if 5 in li:
    print('Sim, o 5 foi digitado e faz parte da lista!')
else:
    print('Nãon o 5 não foi digitado e não faz parte da lista!')