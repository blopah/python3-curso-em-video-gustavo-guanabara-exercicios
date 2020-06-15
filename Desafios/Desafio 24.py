print("""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.\n""")

city1 = input('Digite o nome de uma cidade: ')

city = city1.strip().title().split()

# vf = 'Santo' in city[0]

vf = (city[0].find('Santo')) + 1

res = [ 'não tem', 'tem']

# print(res[vf])

print("Sua cidade {} 'Santo' no início do nome.".format(res[vf]))