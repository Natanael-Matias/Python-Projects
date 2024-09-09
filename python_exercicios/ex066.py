'''Crie um programa que leia vários números inteiros. O programa vai
parar quando digitado 999. No final mostre quantos números foram
digitados e qual foi a soma entre eles.'''

s = c = 0
while True:
    n = int(input('Digite um número (999 para parar: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e sua soma é: {s}.')
