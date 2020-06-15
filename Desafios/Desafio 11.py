print('Calculador de tinta!')
a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))

ar = a*l

t = ar / 2

print('Você precisará de {} litros de tinta para pintar esta parede, pois ela tem {} metros quadrados.'.format(t, ar))
