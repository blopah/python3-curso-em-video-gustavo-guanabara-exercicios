print("""Desenvolva um programa que pergunte a distância de uma viagem em km e calcule o preço da passagem, 
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas""")

dis = input('Insira a distância da viagem em km: ')
num = dis.isnumeric()
price = 0
priceTotal = 0
if num == True:
    dist = int(dis)
    if dist > 200:
        price = 0.45
    else:
        price = 0.50
    priceTotal = price * dist
    print('A passagem desta viagem de {}km sairá por R${:.2f}.'.format(dis, priceTotal))
else:
    print('O valor inserido é inválido.')