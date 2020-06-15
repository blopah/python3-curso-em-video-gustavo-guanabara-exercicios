print('''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.''')

print('Cadastro de pessoas:')
keep = 'S'
cont = p18 = h = m20 = 0
while keep in 'Ss':
    iv = sv = kv = False
    age = 0
    sexo = ''
    cont += 1
    print('{:_^100}'.format(f'Cadastro da {cont}ª pessoa'))
    while not iv:
        idade = str(input('Insira a idade: '))
        if idade.isnumeric():
            age = int(idade)
            if age >= 0:
                iv = True
    while not sv:
        sexo = str(input('Insira o sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MFmf':
            sv = True
    if age > 18:
        p18 += 1
    if sexo in 'Mm':
        h += 1
    if age > 20 and sexo in 'Ff':
        m20 += 1
    while not kv:
        keep = str(input('Deseja cadastrar mais pessoas? [S/N]')).strip().upper()[0]
        if keep in 'SNsn':
            kv = True
print(f'Das \033[1;31m{cont}\033[0;0m pessoas cadastradas, \033[1;31m{p18}\033[0;0m são maiores de 18 anos, \033[1;31m{h}\033[0;0m são homens e \033[1;31m{m20}\033[0;0m são mulheres com mais de 20 anos.')
