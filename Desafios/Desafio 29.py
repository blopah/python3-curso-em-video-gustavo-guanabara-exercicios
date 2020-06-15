print("""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80hm/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acimda do limite""")

vel = input('Digite a velocidade do carro: ')
if vel.isnumeric():
    velo = int(vel)
    lim = 80
    dif = velo - 80
    mul = 0
    if dif > 0:
        mul = dif * 7
        print('Você está acima do limite de {}Km/h! Sua multa é de R${},00.'.format(lim, mul))
    else:
        print('Parabéns você está dentro do limite de velocidade.')
else:
    print('Entrada inválida. Digite uma velocidade valida.')
