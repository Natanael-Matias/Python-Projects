'''Criar jogos da MEGA SENA. Perguntar quantos jogos serão feitos e
sortear eleatóreamente 6 números entre 1 e 60. Tudo em uma lista composta.'''

from random import randint

Jogos = list()
palp = list()

n = int(input('Número de jogos que deseja: '))

for j in range(0,n):
	for x in range(0,6):
		e = randint(1,60)
		if e not in palp:
			palp.append(e)
		else:
			x-=1
	palp.sort()		
	Jogos.append(palp[:])
	palp.clear()

for x in range(0,n):
	print(f'Jogo {x+1}: {Jogos[x]}')
