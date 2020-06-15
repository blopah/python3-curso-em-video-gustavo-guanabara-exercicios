print('''Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.''')

turma = [[]]
c = 0
ni = 0
while True:
    nome = input('Nome: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    turma[c].append(nome) #turma = [[nome]]
    turma[c].append([]) #turma = [[nome, []]]
    turma[c][1].append(nota1)
    turma[c][1].append(nota2)
    c += 1
    keep = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while keep not in 'SN':
        keep = input('Opção inválida. Deseja continuar? [S/N] ').strip().upper()[0]
    if keep == 'N':
        break
    # print(turma)
    # print(c)
    turma.append([]) #turma = [[]]

print('{:=<50}'.format(''))
for co in range(0, len(turma), 1):
    print(co, end='  ')
    print(turma[co][0], end='  ')
    print((turma[co][1][0]+turma[co][1][1])/2, end='\n')
    # print(len(turma))
while True:
    ni = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe) :'))
    while ni >= len(turma):
        if ni == 999:
            break
        ni = int(input('Opção inválida. Deseja mostrar as notas de qual aluno? (999 interrompe) :'))
    if ni == 999:
        break
    print(f'As notas de {turma[ni][0]} são {turma[ni][1][0]} e {turma[ni][1][1]}.')
