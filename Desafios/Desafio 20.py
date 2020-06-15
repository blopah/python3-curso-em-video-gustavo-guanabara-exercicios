import random

print('\nO mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. \nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

nomes = 'Márcia Vitória Ariadne Naty'.split()

ordem = random.shuffle(nomes)

print('\nA sequência de apresentação será {}, {}, {} e por fim {}.'.format(nomes[0], nomes[1], nomes[2], nomes[3]))