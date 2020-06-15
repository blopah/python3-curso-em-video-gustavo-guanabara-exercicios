print("""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa mostre:
• A média de idade do grupo.
• Qual é o nome do homem mais velho.
• Quantas mulheres têm menos de 20 anos.""")
p1 = list
p2 = list
p3 = list
hmv = ['Não há nenhum homem na lista.', 0, 'None']
qm20 = 0
for c in range(0, 3, 1):
    # Entradas
    nome = str(input('Qual seu nome?')).strip().capitalize()
    idade = int(input('Qual sua idade?'))
    sexo = str(input('Qual seu sexo?')).strip().capitalize()
    # cadastros
    if c == 0:
        p1 = [nome, idade, sexo]
    if c == 1:
        p2 = [nome, idade, sexo]
    if c == 2:
        p3 = [nome, idade, sexo]
    # hmv
    if c == 0:
        if idade > hmv[1] and sexo == 'Masc':
            hmv = p1
    if c == 1:
        if idade > hmv[1] and sexo == 'Masc':
            hmv = p2
    if c == 2:
        if idade > hmv[1] and sexo == 'Masc':
            hmv = p3
    #qm20
    if idade < 20 and sexo == 'Fem':
            qm20 += 1
            print('Entrou no if qm20')

print(p1)
print(p2)
print(p3)
print('A média de idade do grupo é {:.0f} anos.'.format((p1[1]+p2[1]+p3[1])/3))
# masc1 = masc.split()
if hmv[1] == 0:
    print(hmv[0])
else:
    print('O nome do homem mais velho é {}'.format(hmv[0]))
if qm20 == 0:
    print('Não há mulheres com menos de 20 anos.')
else:
    print('há {} mulher(es) com menos de 20 anos.'.format(qm20))