print('''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.''')

import datetime
dados = dict()
import datetime

now = datetime.datetime.now().year


dados['nome'] = input('Nome: ')
dados['dn'] = int(input('Ano de nascimento: '))
dados['idade'] = now - dados['dn']
dados['ctps'] = input('CTPS: (0 para "Não possui") ')
if dados['ctps'] != '0':
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = str('R$' + str(input('Salário: R$')))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - dados['dn']
for k, v in dados.items():
    print(f'{k} - {v}')