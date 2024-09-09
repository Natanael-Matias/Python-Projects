''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo. '''

''' from math import cos, sin, tan, pi
a = float(input('Digite um ângulo em graus: '))
b = (a * pi)/180
s = sin(b)
c = cos(b)
t = tan(b)

print('sen({}) = {:.2f} \ncos({}) = {:.2f} \ntg({}) = {:.2f}'.format(a, s, a, c, a, t)) '''

import math
a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('sen({}) = {:.2f} \ncos({}) = {:.2f} \ntg({}) = {:.2f}'.format(a, s, a, c, a, t))
