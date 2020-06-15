print("""Crie um programa que leia o nome completo de uma pessoa e mostre: 
1 O nome com todas as letras maiúsculas
2 O nome com todas minúsculas
3 Quantas letras ao todo(sem considerar espaços)
4 Quantas letras tem o primeiro nome.""")

nome = str(input('\nDigite seu nome completo: '))

um = nome.title()
dois = nome.upper()
tres = nome.lower()
quatro = len(nome.replace(' ', ''))
cinco = len(nome.split()[0])

print(um)
print(dois)
print(tres)
print(quatro)
print(cinco)