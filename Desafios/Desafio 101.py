print('''Crie um programa que tenha uma função chamada voto() que 
vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto
NEGADO
OPCIONAL ou
OBRIGATÓRIO nas eleições.\n''')
from datetime import date
# help(datetime)
anoatual = date.today().year
# print(f'{anoatual}')
def voto(dn):
    idade = anoatual - dn
    res = 'Voto OPCIONAL'
    if idade < 16:
        res = 'Voto NEGADO'
    elif idade < 18:
        res = 'Voto OPCIONAL'
    elif idade < 65:
        res = 'Voto OBRIGATÓRIO'
    return res

dn = int(input('Data de nascimento: '))
resultado = voto(dn)
print(f'{resultado}')