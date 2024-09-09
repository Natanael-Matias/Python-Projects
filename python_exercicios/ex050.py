'''Desenvolva um programa que leia seis numeros inteiros, e mostre a soma somente
daqueles que forem pares.'''

s = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        s += n
print('\nA soma somente dos números pares digitados é {}.'.format(s))