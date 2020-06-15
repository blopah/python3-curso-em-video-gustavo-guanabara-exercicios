print("""Faça um programa que leia três números e mostre qual é o maior e qual é o menor.""")

a = input('Digite um número real: ')
b = input('Digite outro número real: ')
c = input('Digite mais um número real: ')

ok = (a.isnumeric() and b.isnumeric() and c.isnumeric())

if ok == True:
    a = int(a)
    b = int(b)
    c = int(c)

    if a > b:
        if b > c:
            print('{}a, {}b, {}c.'.format(a, b, c))
        else:
            if a > c:
                print('{}a, {}c, {}b.'.format(a, c, b))
            else:
                print('{}c, {}a, {}b.'.format(c, a, b))
    else:
        if a > c:
            print('{}b, {}a, {}c.'.format(b, a, c))
        else:
            if b > c:
                print('{}b, {}c, {}a.'.format(b, c, a))
            else:
                print('{}c, {}b, {}a.'.format(c, b, a))

else:
    print('Entrada invalida')