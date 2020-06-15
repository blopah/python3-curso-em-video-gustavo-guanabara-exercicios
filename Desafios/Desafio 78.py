print('''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado 
e as respectivas posições na lista.''')
li = []
for c in range(1, 6, 1):
    li.append(int(input(f'Digite o {c}º valor: ')))
lio = li[:]
lio.sort()
print(f'O maior valor da lista é o {lio[-1]} que está nas posições: ', end='')
for c in enumerate(li):
    if lio[-1] == c[1]:
        print(c[0] + 1, end='ª ')
print('da lista.')
print(f'O menor valor da lista é o {lio[0]} que está nas posições: ', end='')
for c in enumerate(li):
    if lio[0] == c[1]:
        print(c[0] + 1, end='ª ')
print('da lista.')
