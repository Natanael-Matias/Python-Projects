'''Crie um programa que vai gerar 5 númreos aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior que estão na tupla.'''

from random import randint
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = maior = t[0]
for c in range(1, 5):
    if t[c] < menor:
        menor = t[c]
    if t[c] > maior:
        maior = t[c]
print(f'Os valores gerados são: {t}. \nO maior é {maior} e o menor é {menor}.')
