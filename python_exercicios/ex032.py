'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

from datetime import date
ano = int(input('Digite um ano qualquer \nOu 0 para ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano {} é Bissexto.'.format(ano))
else:
    print('Ano {} não é bissexto.'.format(ano))
