''' Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ferramentas import moeda

num = float(input('Digite um valor: R$'))

print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}')
