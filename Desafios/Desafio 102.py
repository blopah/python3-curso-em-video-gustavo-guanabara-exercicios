print('''Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: 
O primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de calculo do fatorial.\n''')

def fatorial(n, show=False):
    '''
    Criado por PLX
    :param n: O número a ser calculado o fatorial
    :param show: (opcional) Se Verdadeiro, mostra os calculos da conta.
    :return: Printa o resultado dependendo do param show
    '''
    calc = str()
    x = n
    for i in range(x-1, 0, -1):
        calc += str('x')
        x = x * i
        calc += str(i)
    if show:
        print(f'O fatorial de {n} é {n}{calc}={x}')
    else:
        print(f'O fatorial de {n} é {x}')

fatorial(5, show = True)
help(fatorial)