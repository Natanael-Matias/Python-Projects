''' Faça um programa que leia um número de 0 a 9999 e mostre na tela
 cada um dos dígitos e sua posição decimal'''

num = int(input('Type a number between 0 and 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A unidade de milhar será: {}'.format(m))
print('A unidade de centena será: {}'.format(c))
print('A unidade de dezena será: {}'.format(d))
print('A unidade será: {}'.format(u))
