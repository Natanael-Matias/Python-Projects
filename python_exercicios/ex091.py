# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário 
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
ranking = list()

for n in range(0,4):
	a = randint(1,6)
	jogador[f'Jogador {n+1}'] = a

print('*'*5, 'VALORES SORTEADOS', '*'*5)

for k, v in jogador.items():
	print(f'{k} : {v}')
	sleep(1)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True) # key=itemgetter(x) : x = 0 -> chave do dict indicado; x = 1 -> Valor do dict indicado

print('*'*5, 'RANKING', '*'*5)

for i,v in enumerate(ranking):
	print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
	sleep(1)