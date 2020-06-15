print("""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
• Se ele ainda vai se alistar ao serviço militar.
• Se é a hora de se alistar.
• Se já passou o tempo do alistamento.r
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.""")

from datetime import date

dn = int(input('Insira o ano de seu nascimento: '))
data = date.today().year
ida = data - dn

if ida > 18 :
    print('Você ja passou {} ano(s) da idade de se alistar'.format((ida - 18)))
elif 18 > ida :
    print('Ainda falta(m) {} ano(s) para você se alistar'.format(18 - ida))
else:
    print('É hora de se alistar! Você já tem {} anos!'.format(ida))
