print('''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.''')

print('{:-^40}'.format('Digite 10 palavras!'))
li = []
for c in range(1, 11, 1):
    palavra = str(input(f'Digite a {c}ª palavra: ')).strip().upper()
    li.append(palavra)
tu = (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7], li[8], li[9])
# print(li)
# print(tu)
for letra in tu:
    print(f'Na palavra \033[1;31m{letra}\033[0;0m temos as vogais: ', end='')
    for c in range(0, len(letra), 1):
        if letra[c] in 'aeiouAEIOU':
            print('\033[1;34m', letra[c], '\033[0;0m', end=' ')
    print('.')
