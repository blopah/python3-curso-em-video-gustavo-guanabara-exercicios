print("""Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente 
até ter um valor correto.""")
s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    # print(s)
    if s != 'M' and s != 'F':
        print('Sexo inválido. Tente novamente.')
print('Ok!')