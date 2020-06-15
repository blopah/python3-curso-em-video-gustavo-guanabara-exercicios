print('''Faça um programa que tenha uma função chamada área(), que
receba as dimensões de um terreno retangular (largura e comprimento)
 e mostre a área do terreno''')

def area(a, l):
    area = a*l
    return area

print('{:-^30}'.format('Controle de Terreno'))
a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))

area = area(a, l)
print(f'Este terreno tem {area:.2f}m².')