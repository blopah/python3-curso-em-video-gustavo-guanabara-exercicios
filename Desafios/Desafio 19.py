import random

print('\nUm professor quer sortear um dos seus quatro alunos para apagar o quadro. \nFaça um programa que ajude ele, lendo o nome do escolhido.')

al1 = str('Vitória')
al2 = str('Márcia')
al3 = str('Naty')
al4 = str('Ariadne')

selec = str(random.choice([al1, al2, al3, al4]))

print('\n A garota sorteada é a {:=^15}!'.format(selec))