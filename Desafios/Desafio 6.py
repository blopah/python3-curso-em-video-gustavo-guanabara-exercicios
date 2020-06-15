print('Este programa mostra o dobro, o triplo e a raiz quadrada do número que você digitar. \n')

n = float(input('Digite um número:'))
d = n * 2
t = n * 3
r = float(n ** 0.5)

print('\nO dobro é "{}" o triplo é "{}" e a raiz quadrada é "{:.3}"'.format(d, t, r))