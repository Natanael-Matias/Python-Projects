'''Faça um programa que leia um número e diga se ele é ou não um número primo.'''

n = int(input('Digite um número: '))
np = 0

for c in range(1, n):
    if n % c == 0:
        np += 1

if np > 1:
    print('O número digitado NÃO é primo.  {}'.format(np))
else:
    print('O número digitado é primo.  {}'.format(np))
