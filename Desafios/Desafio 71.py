print('''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$50,00 R$20,00 R$10,00 E R$1,00''')

print('\n{:$^100}\n'.format("- Bem vindo ao Blopa's Bank! -"))

while True:
    saq = str(input(('Qual valor desejas sacar? ')))
    if saq.isnumeric():
        saq = int(saq)
        break
c = v = d = u = 0
c = saq // 50
if saq % 50 != 0:
    v = (saq % 50) // 20
if ((saq % 50) % 20) != 0:
    d = ((saq % 50) % 20) // 10
if (((saq % 50) % 20) % 10) != 0:
     u = (((saq % 50) % 20) % 10)

print('Você receberá:')
if c > 0:
    print(f'{c} notas de R$50,00')
if v > 0:
    print(f'{v} notas de R$20,00')
if d > 0:
    print(f'{d} notas de R$10,00')
if u > 0:
    print(f'{u} notas de R$1,00')
print('')

print('{:$^100}'.format("- Muito obrigado por utilizar o Blopa's Bank! -"))