print("""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.""")
from time import sleep
print("Atenção para o ano novo em...")
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("Feliz ano novo!")