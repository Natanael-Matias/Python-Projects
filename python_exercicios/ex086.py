'''Criar uma matriz 3x3 preenchida pelo teclado.'''

M = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3): #Linhas
	for j in range(0,3): #Colunas
		M[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))

for i in range(0,3):
	for j in range(0,3):
		print(f'{M[i][j]:^5}\t', end='') # :^5 -> centraliza(^) entre 5 espaços
	print('\n')
