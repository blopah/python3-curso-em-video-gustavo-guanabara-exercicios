print('''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.''')

li = [[],[]]
for c in range(1, 7, 1):
    nop = noi = 1
    valor = int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 0:
        if len(li[0]) == 0:
            li[0].append(valor)
        else:
            for c in range(0, len(li[0]), 1):
                if valor < li[0][c]:
                    li[0].insert(c, valor)
                    nop = 0
                    break
            if nop == 1 and len(li[0]) > 0:
                li[0].append(valor)
    else:
        if len(li[1]) == 0:
            li[1].append(valor)
        else:
            for d in range(0, len(li[1]), 1):
                if valor < li[1][d]:
                    li[1].insert(d, valor)
                    noi = 0
                    break
            if noi == 1 and len(li[1]) > 0:
                li[1].append(valor)
print(f'li = {li}')
print(f'li par = {li[0]}')
print(f'li impar = {li[1]}')
