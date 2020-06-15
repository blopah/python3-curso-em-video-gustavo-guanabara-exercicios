print("""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome""")

nome1 = input('Digite seu nome: ')

nome = nome1.strip().title()

b = 'Silva' in nome

c = ['não tem', 'tem']

# print(c[b])
print('Você {} Silva no nome.'.format(c[b]))