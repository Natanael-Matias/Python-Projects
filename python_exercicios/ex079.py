'''Faça um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

var = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in var:
        var.append(n)
    op = input('Deseja continuar: [S/N]: ').upper()
    while op not in 'SN':
        op = input('Deseja continuar: [S/N]: ').upper()
    if op == 'N':
        break

var.sort()
print(f'Os valores digitados, em ordem, são {var}')
