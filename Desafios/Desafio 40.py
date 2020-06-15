print("""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atengida:
• Média abaixo de 5.0: REPROVADO
• Média entre 5.0 e 6.9: RECUPERAÇÃO
• Média 7.0 ou superior: APROVADO""")

n1 = float(input('Insira a primeira nota: \n'))
n2 = float(input('Insira a segunda nota: \n'))

med = ((n1 + n2) / 2)

if med < 5:
    print('Sua média foi {:.1f} e você está REPROVADO.'.format(med))
elif med < 7:
    print('Sua média foi {:.1f} e você está RECUPERAÇÃO'.format(med))
elif med >= 7:
    print('Sua média foi {:.1f} e você está APROVADO'.format(med))