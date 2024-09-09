'''Refazer o ex 51 lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.'''

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a = 0
s = []
while a < 10:
    s.append(n1 + a * r)
    a += 1
print(s)
