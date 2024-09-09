'''Crie um programa que faça o computador jogar JOKENPÔ com você.'''

from time import sleep
from random import choice
pc = ['Pedra', 'Papel', 'Tesoura']
us = input('Escolha: Pedra, Papel ou Tesoura: ').capitalize()
e = choice(pc)

print('\033[32mJO\033[m')
sleep(0.5)
print('\033[36mKEN\033[m')
sleep(0.5)
print('\033[33mPO!!!\033[m')
sleep(0.5)

print('\033[33m*=\033[m' * 15)
print('\033[34mComputador jogou {}\033[m'.format(e))
print('\033[34mVocê jogou {}'.format(us))
print('\033[33m*=\033[m' * 15)

if us == 'Pedra' or us == 'Papel' or us == 'Tesoura':
    if us == e:
        print('Empate!!!')
    elif us == 'Pedra' and e == 'Papel':
        print('\033[31mYOU LOSE!!!\033[m')
    elif us == 'Pedra' and e == 'Tesoura':
        print('\033[34mYOU WIN!!!\033[m')
    elif us == 'Papel' and e == 'Pedra':
        print('\033[34mYOU WIN!!!\033[m')
    elif us == 'Papel' and e == 'Tesoura':
        print('\033[31mYOU LOSE!!!\033[m')
    elif us == 'Tesoura' and e == 'Pedra':
        print('\033[31mYOU LOSE!!!\033[m')
    elif us == 'Tesoura' and e == 'Papel':
        print('\033[34mYOU WIN!!!\033[m')
else:
    print('Jogada Inválida.')
