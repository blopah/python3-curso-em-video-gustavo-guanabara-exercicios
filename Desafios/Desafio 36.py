print("""Escreve um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar 
• o valor da casa, 
• o salário do comprador 
• e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.""")

import math

val = float(input('\033[1;30;0mInsira o valor da casa: \033[m'))
sal = float(input('\033[1;30;0mInsira o salario do comprador: \033[m'))
anos = int(input('\033[1;30;0mInsira os anos para pagamento: \033[m'))

prest = val / (anos*12)
anosn = (val / (sal*0.3)) / 12
saln = (val / (anos * 12)) * 3.33

if prest > (sal*0.3):
    print("""\033[1;31;0mInfelizmente seu empréstimo foi negado.\033[m 
\033[1;31;0mPois a parcela de \033[4;31;0mR${:.2f}\033[1;31;0m corresponde a mais de \033[4;31;0m30%\033[1;31;0m do seu salário que é \033[4;31;0mR${:.2f}\033[1;31;0m.\033[m
\033[1;31;0mVocê precisa de no mínimo \033[4;31;0m{} anos\033[1;31;0m para conseguir quitar esta casa com o salario atual.\033[m
\033[1;31;0mOu então um salário de \033[4;31;0m{:.2f}\033[1;31;0m para conseguir quitar esta casa em \033[4;31;0m{} ano(s)\033[m\033[1;31;0m.\033[m""".format(math.ceil(prest), (sal*0.3), math.ceil(anosn), math.ceil(saln), anos))
else:
    print("""\033[1;32;0mParabéns! Você conseguiu o empréstimo!
Sua parcela será de \033[4;32;0mR${:.2f}\033[1;32;0m mensais para pagar em \033[4;32;0m{} anos\033[1;32;0m.\033[m""".format(prest, anos))