print("""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
• Abaixo de 18.5: Abaixo do peso
• Entre 18.5 e 25: Peso ideal
• 25 até 30: Sobrepeso
• 30 até 40: Obesidade
• Acima de 40: Obesidade mórbida""")

from math import pow

nome = input('Insira seu nome: ').strip().capitalize()
alt = float(input('Insira sua altura em metros: '))
pes = float(input('Insira seu peso em Kg: '))

imc = pes / pow(alt, 2)

if nome == 'Vitória':
    print('Seu IMC é de \033[7m{:.2f}\033[m. Você está gostosa.'.format(imc))
else:
    if imc < 18.5:
        print('Seu IMC é de \033[7m{:.2f}\033[m. Você está abaixo do peso.'.format(imc))
    elif imc < 25:
        print('Seu IMC é de \033[7m{:.2f}\033[m. Você está no peso ideal.'.format(imc))
    elif imc < 30:
        print('Seu IMC é de \033[7m{:.2f}\033[m. Você está com sobrepeso.'.format(imc))
    elif imc < 40:
        print('Seu IMC é de \033[7m{:.2f}\033[m. Você está obeso(a).'.format(imc))
    elif imc >= 40:
        print('Seu IMC é de \033[7m{:.2f}\033[m. Você está obeso(a) mórbido(a).'.format(imc))