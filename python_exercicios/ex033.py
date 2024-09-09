'''Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.'''

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('maior: {} \nmenor: {}'.format(maior, menor))