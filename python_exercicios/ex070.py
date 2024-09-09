'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o produto mais barato.'''

t = c = 0
produtos = []
while True:
    prod = input('Nome do produto: ').capitalize()
    if prod == '':
        print('Entrada Inválida!!!')
        continue
    preco = float(input('Valor: R$'))
    produtos.append(prod)
    produtos.append(preco)
    t += preco
    if preco >= 1000:
        c += 1
    op = input('Deseja Continuar? [S/N] ').upper()
    while op not in 'SN' or op == '':
        print('Entrada Inválida!!!')
        op = input('Deseja Continuar? [S/N] ').upper()
    mb = produtos[0]
    menor = produtos[1]
    if op == 'N':
        for a in range(1, len(produtos), 2):
            if produtos[a] < menor:
                menor = produtos[a]
                mb = produtos[a - 1]

        print(f'''\nO total gasto foi R${t:.2f}.
{c} produto(s) custa(m) mais de R$1000,00.
O produto mais barato foi {mb} e custou R${menor:.2f}.''')
        break
