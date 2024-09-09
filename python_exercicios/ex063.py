'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de Fibonacci.'''

n = int(input('Número de termos da sequência de Fibonacci: '))
f = [0, 1]
a = 0
while a < n:
    f.append(f[a] + f[a + 1])
    a += 1
print(f[:n])
