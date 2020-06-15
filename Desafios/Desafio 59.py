print("""\033[1;30mCrie um programa que leia dois valores e mostre
 um menu na tela:
 [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso.\n\033[0;0m""")

n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
op = ''

while op != '5':
    op = str(input("""Escolha uma opção: \n [1] Somar\n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa\n"""))
    if op == '1':
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, (n1 + n2)))
    elif op == '2':
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, (n1 * n2)))
    elif op == '3':
        print('O maior número inserido é {}.'.format(n1 if n1 > n2 else n2))
    elif op == '4':
        n1 = int(input('Insira o 1º número: '))
        n2 = int(input('Insira o 2º número: '))
    elif op == '5':
        print('Você escolheu [{}] Sair do programa. \nObrigado por usar os softwares Blopa.'.format(op))
    else:
        print('Opção inválida [{}]. Tente novamente.'.format(op))