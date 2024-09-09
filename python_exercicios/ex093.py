''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''

jogador = dict()

jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Gols'] = list()
N = int(input('Nº de partidas jogadas: '))
jogador['Total'] = 0

for i in range(0,N):
	gol = int(input(f'Nº de gols na partida {i+1}: '))
	jogador['Gols'].append(gol)
	jogador['Total'] = jogador['Total'] + gol

print(40*'-*')
print(f'O jogador {jogador["Nome"]} participou de {N} partidas.')
for i in range(0,N):
	print(f'	-> Partida {i+1}: {jogador["Gols"][i]} gols')
print(f'Com um total de {jogador["Total"]} gols.')
