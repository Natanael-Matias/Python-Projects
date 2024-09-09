'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

Clube = list()
jogador = dict()

while True:
	jogador.clear()
	jogador['Nome'] = str(input('Nome do Jogador: '))
	N = int(input('Nº de partidas jogadas: '))
	jogador['Gols'] = list()

	for i in range(0,N):
		gol = int(input(f'Nº de gols na partida {i+1}: '))
		jogador['Gols'].append(gol)
	
	jogador['Total'] = sum(jogador['Gols'])
	Clube.append(jogador.copy())

	while True:
		new = str(input('Novo Jogador? [S/N]: ')).upper()
		if new in 'SN':
			break
		print('ERRO! Digite S ou N.')
	if new == 'N':
		print('ENCERRADO!')
		break

print(20*'-=')
print('Cod.',end=' ')
for k in Clube[0].keys():
	print(f'{k:<15}',end=' ')
print()
print(40*'-')

for i, d in enumerate(Clube):
	print(f'{i+1:<4}',end=' ')
	for v in d.values():
		print(f'{str(v):<15}',end=' ')
	print()
print(40*'-')

while True:
	cod = int(input('Digite o código de um jogador [0 p/ sair]: '))
	if cod == 0:
		print('Programa Finalizado!')
		break
	elif cod > len(Clube) or cod < 0:
		print('Código inválido!')
	elif cod <= len(Clube):
		print(40*'-')
		print(f'Jogador: {Clube[cod-1]["Nome"]}')
		for k in range(0,len(Clube[cod-1]['Gols'])):
			print(f'Partida {k+1}: {Clube[cod-1]["Gols"][k]} gols.')
		print(40*'-')
