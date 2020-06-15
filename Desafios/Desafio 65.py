print("""\033[1;30mCrie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valor lido. 
O programa deve perguntar ao usuário se ele quer ou não continuar 
a digitar valores.\033[0;0m""")

cont = 0
n = int(input('Digite um valor: '))
r = 'S'
s = 0
i = 1
li = []
while r == 'S':
    i = 1
    cont += 1
    s += n
    li.append(n)
    while i == 1:
        r = str(input('Deseja continuar inserindo valores? [S/N] ')).strip().upper()
        if r == 'S':
            n = int(input('Digite outro valor: '))
            i = 0
        elif r == 'N':
            r = 'N'
            i = 0
        else:
            print('Resposta inválida. Por favor responda denovo.')
            i = 1
li.sort()
print('A média de todos os valores inseridos é {:.1f}.'.format(s / cont))
print('O maior número digitado foi {} e o menor foi {}.'.format(li[-1],li[0]))
# print(s)
# print(cont)
# print(len(li))
# print(li)