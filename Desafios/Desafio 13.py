print('Calculadora de aumento')

sa = float(input('Digite o salario atual: R$'))
a = float(input('Digite o aumento em porcentagem(%): '))

sn = sa * ((100+a)/100)

print('O salario novo é de R${:.2f}.'.format(sn))