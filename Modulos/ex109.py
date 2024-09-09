''' Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ferramentas import moeda

num = float(input('Digite um valor: R$'))

print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10)}')