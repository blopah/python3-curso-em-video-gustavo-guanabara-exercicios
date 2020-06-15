print("""Elabore umprograma que calcule o valor a ser pago por um produto, 
considerando o seu \033[1;31mpreço normal\033[0;0m e \033[1;31mcondição de pagamento\033[0;0m:
\033[1;31m-\033[0;0m à vista \033[1;34mdinheiro/cheque:\033[0;0m \033[1;31m10%\033[0;0m de desconto
\033[1;31m-\033[0;0m à vista no \033[1;34mcartão\033[0;0m: \033[1;31m5%\033[0;0m de desconto
\033[1;31m-\033[0;0m em até \033[1;34m2x no cartão\033[0;0m: preço normal
\033[1;31m-\033[0;0m \033[1;34m3x ou mais no cartão\033[0;0m: \033[1;31m20%\033[0;0m de juros""")

# Elabore umprograma que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# 1 à vista dinheiro/cheque: 10% de desconto
# 2 à vista no cartão: 5% de desconto
# 3 em até 2x no cartão: preço normal
# 4 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('@blopadesign'))
valor = float(input('Insira o valor total da compra: '))
print("""Escolha a forma de pagamento:
\033[1;31m1\033[0;0m à vista \033[1;34mdinheiro/cheque:\033[0;0m \033[1;31m10%\033[0;0m de desconto
\033[1;31m2\033[0;0m à vista no \033[1;34mcartão\033[0;0m: \033[1;31m5%\033[0;0m de desconto
\033[1;31m3\033[0;0m em até \033[1;34m2x no cartão\033[0;0m: preço normal
\033[1;31m4\033[0;0m \033[1;34m3x ou mais no cartão\033[0;0m: \033[1;31m20%\033[0;0m de juros""")
forma = int(input(''))
valorfinal = 0
if forma == 1:
    print('Sua compra sairá por R${:.2f}. Obrigado!'.format(valor - (valor * 10/100)))
elif forma == 2:
    print('Sua compra sairá por R${:.2f}. Obrigado!'.format(valor - (valor * 5/100)))
elif forma == 3:
    print('Sua compra sairá por R${:.2f}. Obrigado!'.format(valor))
elif forma == 4:
    print('Sua compra sairá por R${:.2f}. Obrigado!'.format(valor + (valor * 20/100)))
else:
    print('Entrada invalida')