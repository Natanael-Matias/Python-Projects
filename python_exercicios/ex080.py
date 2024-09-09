'''Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o .sort()).
No final, mostre a lista ordenada na tela.'''

val = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > val[-1]:
        val.append(n)
    else:
        i = 0
        while i < len(val):
            if n < val[i]:
                val.insert(i, n)
                break
            i += 1
print(val)
