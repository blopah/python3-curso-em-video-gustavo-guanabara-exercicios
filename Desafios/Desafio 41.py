print("""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
• Até 9 anos: MIRIM
• Até 14 anos: INFANTIL
• Até 19 anos: JUNIOR
• Até 25 anos: SÊNIOR
• Acima: MASTER""")

from datetime import date

dn = (input('Em que ano você nasceu??'))

data = date.today().year

ok = dn.isnumeric()

if ok == True:
    dn = int(dn)
    ida = data - dn
    if ida < 9:
        print('Você tem {} anos então ua categoria é MIRIM'.format(ida))
    elif ida < 14:
        print('Você tem {} anos então ua categoria é INFANTIL'.format(ida))
    elif ida < 19:
        print('Você tem {} anos então ua categoria é JUNIOR'.format(ida))
    elif ida < 25:
        print('Você tem {} anos então ua categoria é SÊNIOR'.format(ida))
    else:
        print('Você tem {} anos então ua categoria é MASTER'.format(ida))
else:
    print('Entrada inválida')
