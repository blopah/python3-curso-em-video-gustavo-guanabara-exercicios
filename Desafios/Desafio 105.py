print('''Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos e vai retornar 
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)
Adicione também as docstrings da função.\n''')

def notas(*n, sit=False):

    """
    :param n: aqui, insira as notas
    :param sit: (opcional) True para retornar a situação da turma
    :return: analise de notas + se sit == True, situação da turma
    """

    maior = n[0]
    menor = n[0]
    soma = 0
    res = dict()
    for c in n:
        soma += c
        if c > maior:
            maior = c
        # print(f'c={c}, n={n}, maior={maior}')
        if c < menor:
            menor = c
        # print(f'c={c}, n={n}, maior={maior}')
    media = soma / len(n)
    res['maior'] = maior
    res['menor'] = menor
    res['soma'] = soma
    res['media'] = media
    if sit:
        if media > 7:
            res['situacao'] = 'BOA!'.upper()
        elif media >= 5:
            res['situacao'] = 'Media!'.upper()
        elif media < 5:
            res['situacao'] = 'Ruim!'.upper()
    for k, v in res.items():
        print(f'A {k} foi {v}')


notas(3.5, 2, 6.5, 2, 7, 4, sit=True)