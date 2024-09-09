'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
n = 0
m = 0
ano = date.today().year

for c in range(1, 8):
    idd = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - idd >= 21:
        n += 1
    else:
        m += 1
print('{} pessoas possuem 21 anos ou mais.'.format(n))
print('{} pessoas AINDA NÃO possuem 21 anos ou mais.'.format(m))