''' Aprimorar o desafio anterior mostrando no final:
 a) A soma de todos os valores pares digitados
 b) A soma dos valores da terceira coluna
 c) O maior valor da segunda linha.'''

M = [[0,0,0],[0,0,0],[0,0,0]]
s0 = 0
s1 = 0
m = 0
for i in range(0,3):
    for j in range(0,3):
        M[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(0,3):
    for j in range(0,3):
        if M[i][j] % 2 == 0:
            s0 += M[i][j]
        if j == 2:
            s1 += M[i][j]
        if i == 1:
            if M[i][j] > m:
                m = M[i][j]

print(20*'-=')

for i in range(0,3):
    for j in range(0,3):
        print(f'{M[i][j]:^5}\t', end='')
    print()

print(20*'-=')

print(f'''A soma de todos os valores pares digitados: {s0}
A soma dos valores da terceira coluna: {s1}
O maior valor da segunda linha: {m} ''')