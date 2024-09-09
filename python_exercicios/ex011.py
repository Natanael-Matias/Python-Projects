# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m^2.

l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
q = a / 2

print('A área da parede é {} metros quadrados e serão necessários {} litros de tinta para pintá-la'.format(a, q))
