'''Melhorar o desafio 28 onde o comutador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

from random import randint
c = 1
n = randint(0, 10)
u = int(input('Digite um valor de 0 qa 10: '))
while n != u:
    if n < u:
        u = int(input('MENOS... Tente novamente: '))
    else:
        u = int(input('MAIS... Tente novamente: '))
    c += 1
print('Você acertou!!!\nParabéns!!!')
print('Você precisou de {} tentativas.'.format(c))
