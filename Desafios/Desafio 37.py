print("""Escreva um programa que leia um número inteiro qualquer e paçe para o usuário escolher qual será a base de conversão:
• 1 para binário
• 2 para octal
• 3 para hexadecimal""")

num = int(input('Digite um número:\n'))

print("""1 para BINÁRIO
2 para OCTAL
3 para HEXADECIMAL""")

op = int(input('Qual será a base de conversão?\n'))

if op == 1 :
    print('O número {} em BINÁRIO fica {}'.format(num, bin(num)[2]))
elif op == 2 :
    print('O número {} em OCTAL fica {}'.format(num, oct(num)[2]))
elif op == 3 :
    print('O número {} em HEXADECIMAL fica {}'.format(num, hex(num)[2]))
else:
    print('Entrada inválida.')