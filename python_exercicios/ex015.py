# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por km rodado.

km = float(input('Quilômetros rodados: '))
d = int(input('Dias alugados: '))
p = d * 60 + km * 0.15

print('Total a pagar: R${:.2f}'.format(p))
