print('''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla''')
from random import randint
num = (int(randint(0, 9)), int(randint(0, 9)), int(randint(0, 9)), int(randint(0, 9)), int(randint(0, 9)))
print(f'Os números gerados foram: {num[0]}, {num[1]}, {num[2]}, {num[3]} e {num[4]}.')
print(f'O maior número gerado foi {sorted(num)[-1]}')
print(f'O menor número gerado foi {sorted(num)[0]}')
