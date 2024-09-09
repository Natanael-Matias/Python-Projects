'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.'''

val = list()
for c in range(0, 5):
    val.append(int(input(f'Digite o {c + 1}º valor: ')))
maior = menor = val[0]

for c in range(0, 5):
    if val[c] > maior:
        maior = val[c]
    if val[c] < menor:
        menor = val[c]

print(f'Os valores digitados foram: {val}')
print(f'O maior foi {maior} na(s) posição(ões):', end='')
for i, v in enumerate(val):
    if v == maior:
        print(f'...{i + 1}', end='')

print(f'\nO menor foi {menor} na(s) posição(ões):', end='')
for i, v in enumerate(val):
    if v == menor:
        print(f'...{i + 1}', end='')
