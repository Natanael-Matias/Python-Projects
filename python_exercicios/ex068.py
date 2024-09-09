'''Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.'''

from random import randint
c = 0
pi = ''
while True:
    comp = randint(0, 10)
    us = int(input('Digite um número: '))
    op = input('Par ou Ímpar [P/I]: ').upper()
    result = comp + us
    if op not in 'PI' or op == '':
        print('Entrada Inválida!!!')
        continue
    if result % 2 == 0:
        pi = 'P'
    else:
        pi = 'I'
    if pi == op:
        print(f'Você Venceu. Eu escolhi {comp}.')
        c += 1
    else:
        print(f'Depois de {c} vitória(s), você perdeu. Eu escolhi {comp}.')
        break
