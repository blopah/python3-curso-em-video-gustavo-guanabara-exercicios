print('''Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for 
negativo.''')

while True:
    n = int(input('Quer ver a taboada de qual número? '))
    c = 0
    if n < 0:
        break
    for c in range(0, 10, 1):
        c += 1
        r = n * c
        print(f'{n} * {c} = {r}')
    print('{:-^100}'.format('FIM'))
print('{:-^100}'.format('Obrigado por utilizar os softwares Blopa'))