print('''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.''')

exp = str(input('Insira uma expressão: '))
pt = 0
for c in enumerate(exp):
    if c[1] == '(':
        pt += 1
    if c[1] == ')':
        pt -= 1
    if pt == -1:
        print('O parênteses em vermelho está errado.')
        print(exp[:c[0]], end='')
        print('\033[1;31m', exp[c[0]], '\033[0;0m', end='')
        print(exp[(c[0]+1):], end='')
        break
if pt == 0:
    print('Está certinho')
elif pt > 0:
    print('Estão faltando parenteses.')