print('Este programa mostra a nota média do aluno em 4 meses. \n')

nome = str(input('Qual o nome do aluno? '))

fev = float(input('Nota de fevereiro: '))
mar = float(input('Nota de março: '))
abr = float(input('Nota de abril: '))
mai = float(input('Nota de maio: '))

media = float((fev + mar + abr + mai)/4)

print('\nA média de {} é de "{:.3}"'.format(nome, media))