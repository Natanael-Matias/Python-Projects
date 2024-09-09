''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa. '''

from math import sqrt, hypot
c1 = float(input('Primeiro cateto: '))
c2 = float(input('Segundo cateto: '))
h = sqrt(c1 ** 2 + c2 ** 2)
hi = hypot(c1, c2)
print('A hipotenusa vale: {:.2f} (ou ainda: {:.2f})'.format(h, hi))
