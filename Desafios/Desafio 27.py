print("""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.""")

nome = input('Digite seu nome completo: ').strip().title()

name = nome.split()

l = len(name) - 1

# print(name[l])
# print(name[0])

print('Olá {} {}! Seja bem vindo(a) ;).'.format(name[0], name[l]))