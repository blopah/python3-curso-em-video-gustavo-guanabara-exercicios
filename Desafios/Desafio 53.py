print("""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.""")
esarf = str('')
frase = str(input('Insira a frase: ')).replace(" ", "").upper()
for c in range(-1, ((len(frase)+1)*(-1)), -1):
    esarf += frase[c]

print(esarf)
print(frase)

if frase == esarf:
    print('As frases são palíndromos!')
else:

    print('As frases NÃO são palíndromos!')