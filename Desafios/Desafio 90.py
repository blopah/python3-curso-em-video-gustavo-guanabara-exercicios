print('''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.''')

aluno = dict()
aluno['nome'] = str(input('Insira o nome: '))
aluno['nota'] = float(input('Insira a nota: '))
if aluno['nota'] < 7:
    aluno['nota'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'
print(f'''O aluno {aluno['nome']} teve a nota {aluno['nota']} e foi {aluno['situacao']}.''')