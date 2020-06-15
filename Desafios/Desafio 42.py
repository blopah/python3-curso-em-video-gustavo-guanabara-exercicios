print("""Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
• Equilátero: todos os lados iguais
• Isósceles: dois lados iguais
• Escaleno: todos os lados diferentes""")

r1 = int(input('Insira o comprimento de uma reta: \n'))
r2 = int(input('Insira o comprimento de outra reta: \n'))
r3 = int(input('Insira o comprimento da última reta: \n'))

tri = ((r1 + r2) >= r3) and ((r1 + r3) >= r2) and ((r2 + r3) >= r1)

if tri:
    if (r1 == r2) and (r3 == r2):
        print('Equilátero')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma um triângulo')