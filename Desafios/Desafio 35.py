print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.""")

r1 = input('Digite uma reta: ')
r2 = input('Digite outra reta: ')
r3 = input('Digite a ultima reta: ')

ok = r1.isnumeric() and r2.isnumeric() and r3.isnumeric()

if ok == True:
    r1 = int(r1)
    r2 = int(r2)
    r3 = int(r3)
    if ((r1 + r2) > r3):
        if ((r1 + r3) > r2):
            if ((r2 + r3) > r1):
                print('Podem formar um triângulo.')
            else:
                print('Não podem formar um triângulo.')
        else:
            print('Não podem formar um triângulo.')
    else:
        print('Não podem formar um triângulo.')
else:
    print('not Ok')