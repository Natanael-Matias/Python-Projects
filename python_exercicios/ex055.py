'''Faça um programa que leia o peso de cinco pessoas. No final mosrtre qual foi o
maior e o menor peso lidos.'''

p = float(input('Digite o 1º peso: '))
m = p
n = p

for c in range(2, 6):
    p = float(input('Digite o {}º peso: '.format(c)))

    if p > m:
        m = p
    if p < n:
        n = p

print('O maior peso é: {:.1f} kg'.format(m))
print('O menor peso é: {:.1f} kg'.format(n))
