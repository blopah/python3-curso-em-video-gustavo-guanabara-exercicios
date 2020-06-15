print('''Desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os em uma tupla. 
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.''')
li = []
lipar = []
for c in range(0, 4, 1):
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            li.append(num)
            break
        else:
            print('Número inválido. ', end='')
tupla = ('', li[0], li[1], li[2], li[3])
print(f'Os números desta tupla são: {tupla[1:]}')
print(f'Nesta tupla, o Nº9 apareceu {tupla.count(9)}x.')
if 3 not in tupla:
    print('O número 3 não foi digitado nesta tupla.')
else:
    print(f'O número 3 foi digitado pela primeira vez na {tupla.index(3)}ª posição.')
prin = ''
for pares in tupla[1:]:
    if pares % 2 == 0 and pares !=0:
        prin += (str(pares) + ', ')
prin = prin[:-2]
if prin != '':
    print(f'O números pares digitados são: {prin}.')
else:
    print('Não foram digitados números pares nesta Tupla.')