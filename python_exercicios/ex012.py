# Faça um programa que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto.

p = float(input('Preço: '))
d = p - p * 0.05
print('Com 5% de desconto, fica: {:.2f}'.format(d))
