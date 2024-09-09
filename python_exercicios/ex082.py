'''Crie um programa qe vai ler vários números e colocar e uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

v = list()
p = list()
i = list()

while True:
    n = int(input('Digite um valor: '))
    v.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    while op not in 'SN':
        op = input('Deseja continuar? [S/N] ').upper()
    if op == 'N':
        break

print(f'Os valores digitados são {v}.')
print(f'Os valores pares são: {p}')
print(f'Os valores ímpares são: {i}')
