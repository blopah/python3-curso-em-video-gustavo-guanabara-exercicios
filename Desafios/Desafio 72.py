print('''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler pelo teclado(Entre 0 e 20) e mostrá-lo por extenso.''')

nume = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = str(input('Digite um número entre 0 e 20: '))
    if n.isnumeric():
        n = int(n)
        if  -1 < n < 21:
            break
print(f'Você digitou o número {nume[n]}.')