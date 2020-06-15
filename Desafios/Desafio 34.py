print("""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.""")

sal = float(input('Digite o salario: '))
lim = float(1250.00)

if sal > lim:
    saln = (sal*1.1)
    print('O aumento será para R${:.2f}'.format(saln))
else:
    saln = (sal*1.15)
    print('O aumento será para R${:.2f}'.format(saln))
