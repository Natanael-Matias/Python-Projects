''' Escreva um programa que faça o computador pensar em um número
de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido
 pelo computador (o programa deverá escrever na tela se o usuário venceu ou perdeu). '''

from random import randint
from time import sleep
n = randint(0, 5)
print('O computador pensou em um número entre 0 e 5. Qual foi?')
u = int(input('Sua resposta: '))
print('PROCESSANDO...')
sleep(2)
if u == n:
    print('VOCÊ VENCEU!!! PARABÉNS.')
else:
    print('Tente novamente.')
    print('O número era {}'.format(n))
