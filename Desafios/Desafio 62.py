print("""Melhore o Desafio 61, perguntando para o usuário se 
ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos..""")

print("""Exercício 51: 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.""")

pt = int(input('Insira o primeiro termo PA: '))
r = int(input('Insira A razão da PA: '))
c = 0
res = pt
prin = ''
rep = 1
while c < 10:
    res = res + r
    prin += str(res) + ', '
    c += 1
print('Os primeiros 10 termos desta PA são: ({}...)'.format(prin))
while rep == 1:
    acres = int(input('Deseja mostrar mais quantos termos? '))
    if acres > 0:
        c = c - acres
        prin = ''
        while c < 10:
            res = res + r
            prin += str(res) + ', '
            c += 1
        print('Os {} termos a mais desta PA são: ({}...)'.format(acres, prin))
    else:
        print('Obrigado por usar um software Blopa.')
        rep = 0
