'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a idade
- se ele ainda vai se alistar
- se é a hora de se alistar
- se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
cand = int(input('Digite o ano de seu nascimento: '))
dt = atual - cand

if dt < 18:
    print('Você ainda não está em idade de alistamento, faltam {} ano(s)'.format(18 - dt))
elif dt > 18:
    print('Você perdeu o prazo de alistamento, devia ser em {}'.format(atual - (dt - 18)))
else:
    print('Você precisa se alistar IMEDIATAMENTE!')
