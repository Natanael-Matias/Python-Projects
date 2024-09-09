'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

from math import fabs
print('=' * 25, '\n  Analisando triangulos')
print('=' * 25)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if fabs(l1 - l2) < l3 < (l1 + l2):
    print('Estas são medidas de um triângulo!')
else:
    print('Estas NÃO são medidas de um triângulo.')
