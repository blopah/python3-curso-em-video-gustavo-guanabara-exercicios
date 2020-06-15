print("""\033[1;30mFaça um programa que leia um número 
qualquer e mostre o seu fatorial.\033[0;0m\n""")

# Usando while

# n = int(input('Digite um número: '))
# c = n
# r = n
# while c > 1 :
#     c -= 1
#     r =  r * c
#     print(r)
# print('O fatorial de {} é {}'.format(n, r))

# Usando for

n = int(input('Digite um número: '))
r = n
i = str(n)
if n == 1 or n == 0:
    print('O fatorial de {} é 1.'.format(n))
else:
    for c in range((n - 1), 0, -1):
        print('{} * {} = '.format(c, r), end='')
        r = r * c
        print('{}'.format(r))
        i = i + '*' + str(c)
    print('Ou {}!={}={}'.format(n, i, r))
    print('O fatorial de {} é {}.'.format(n, r))
