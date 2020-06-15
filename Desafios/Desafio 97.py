print('''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem 
com tamanho adaptável.''')

def moldura(x):
    size = len(x)+2
    print(f'{"~" * (size)}')
    print(' {}'.format(x))
    print(f'{"~" * (size)}')

txt = input('Emoldure seu texto: ')
moldura(txt)