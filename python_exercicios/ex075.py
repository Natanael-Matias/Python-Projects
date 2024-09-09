'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os
em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares.'''

a = []
for c in range(0, 4):
    a.append(int(input('Digite um valor: ')))
v = (a[0], a[1], a[2], a[3])
'''
c = 0
a = []

for t in range(0, 4):
    if v[t] == 9:
        c += 1
    if v[t] % 2 == 0:
        a.append(v[t])
'''
print(f'O número 9 apareceu {v.count(9)} vez(es).')
if 3 in v:
    print(f'O primeiro valor 3 está na posição {v.index(3) + 1}')
print('Os números pares foram: ', end='')
for n in v:
    if n % 2 == 0:
        print(n, end=' ')
