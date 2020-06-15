n = int(input('Digite um número para ver a taboada dele! '))
m = int(input('A taboada de quantos números? '))+1

print('Tabuada do "{}" em "{}"x:'.format(n, m))

for c in range(0, m, 1):
    print('{}*1 = {}'.format(n, (n*c)))