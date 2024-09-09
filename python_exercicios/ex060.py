'''Faça um programa que calcule o fatorial de um número.'''

a = n = int(input('Digite um número: '))
f = 1
print('{}! = '.format(a), end='')
while n > 0:
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    f = f * n
    n = n - 1
print('{}'.format(f))
