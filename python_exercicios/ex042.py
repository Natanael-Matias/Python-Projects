'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- Equilátro, isósceles, Escaleno.'''

from math import fabs
print('=' * 25, '\n  Analisando triangulos')
print('=' * 25)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if fabs(l1 - l2) < l3 < (l1 + l2):
    if l1 == l2 and l1 == l3:
        print('Estas são medidas de um triângulo EQUILÁTERO!')
    if (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
        print('Estas são medidas de um triângulo ISÓSCELES!')
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Estas são medidas de um triângulo ESCALENO!')
else:
    print('Estas NÃO são medidas de um triângulo.')
