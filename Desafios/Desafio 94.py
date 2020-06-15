print('''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados.txt de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final mostre:
A) Quantas pessoas cadastradas
B)A média de idade.
C)Uma lista com mulheres.
D)Uma lista com idade acima da média.''')

turma = list()
aluno = dict()
while True:
    keep = '1'
    aluno['Nome'] = input('Nome: ').strip().upper()
    aluno['Idade'] = int(input('Idade: '))
    aluno['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    while aluno['Sexo'] not in 'MmFf':
        print('Entrada inválida.')
        aluno['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    turma.append(aluno.copy())
    while keep not in 'SN':
        keep = input('Deseja continuar? [S/N]').strip().upper()[0]
    if keep in 'N':
        break
a = len(turma)
b = 0
c = list()
d = list()
for contador in range(0, len(turma), 1):
    b += int(turma[contador]['Idade'])
    if turma[contador]['Sexo'] in 'F':
        c.append(turma[contador])
b = b / len(turma)
for contador in range(0, len(turma), 1):
    if turma[contador]['Idade'] > b:
        d.append(turma[contador])

print(f'A turma tem {a} alunos.')
print(f'A média de idade desta turma é {b}\n\n')
print('{:=^40}'.format('Lista de mulheres cadastradas\n\n'))
for contador in range(0, len(c), 1):
    for k, v in c[contador].items():
        print(f'{k} = {v} | ', end='')
    print('\n\n')
print('{:=^40}'.format('Lista pessoas com idade acima da média'))
for contador in range(0, len(d), 1):
    for k, v in d[contador].items():
        print(f'{k} = {v} | ', end='')
    print('\n\n')
