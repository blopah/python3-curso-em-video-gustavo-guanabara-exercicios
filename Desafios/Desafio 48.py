print("""Faça um programa que calcule a soma de 
todos os números ímpares que são múltiplos de 
três e que se encontram no intervalo de 1 até 500""")
m3 = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        cont += 1
        m3 += c

print('A soma de todos os {} valores é {}.'.format(cont, m3))