print('''Crie um programa onde o usuário possa digitar cinco 
valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela.''')
li = []
for c in range(1, 6, 1):
    no = 1
    valor = int(input(f'Digite o {c}º valor: '))
    if c == 1:
        li.append(valor)
        print(f'Adicionado à {len(li)}ª posição da lista')
    else:
        for i in enumerate(li):
            if i[1] <= valor:
                li.insert(i[0], valor)
                no = 0
                print(f'Adicionado à {i[0]+1}ª posição da lista')
                break
        if no == 1:
            li.append(valor)
            print(f'Adicionado à {len(li)}ª posição da lista')
print(li)