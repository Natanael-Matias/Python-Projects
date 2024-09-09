''' Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores. '''

from ex097 import escreva

def pyHelp(s):
	from time import sleep

	escreva(f"Acessando o manual do comando '{s}'")
	sleep(1)
	print('\033[0;36m')
	help(s)
	print('\033[m')


while True:
	print('\033[0;31m')
	escreva('SISTEMA DE AJUDA PyHELP')
	print('\033[m')

	com = str(input('Função ou Biblioteca > ')).lower()
	if com in 'sair':
		break
	else:
		pyHelp(com)

