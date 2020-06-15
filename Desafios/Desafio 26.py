print("""Faça um programa que leia uma frase pelo teclado e mostre:
1 Quantas vezes aparece a letra 'A'.
2 Em que posição ela aparece a primeira vez.
3 Em que posição ela aparece a última vez.""")

frase1 = input('Digite uma frase: ')
frase = frase1.strip().upper()

um = frase.count('A')

dois = frase.find('A')

tres = frase.rfind('A')

print("""1 A letra 'A' aparece {} vezes. 
2 A primeira vez que ela aparece é na posição {}. 
3 A ultima vez que ela aparece é na posição {}""".format(um, dois, tres))