'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo.
Desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).upper()
sp = frase.split()
jt = ''.join(sp)
pp = ''
n = len(jt)

for a in range(n - 1, -1, -1):
    pp += jt[a]

if pp == jt:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada NÃO é um palíndromo.')
