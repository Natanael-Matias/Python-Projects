''' Ad apte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''

from ferramentas import moeda

num = float(input('Digite um valor: R$'))

print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
