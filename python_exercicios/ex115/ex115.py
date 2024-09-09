from Modulos.interface import *
from Modulos.arquivo import *

arq = 'Cadastros.txt'
if not arqExiste(arq):
	arqCriar(arq)


while True:
	titulo('MENU PRINCIPAL')
	print('\033[33m1\033[m - \033[32mVer pessoas cadastradas\033[m')
	print('\033[33m2\033[m - \033[32mCadastrar nova pessoa\033[m')
	print('\033[33m3\033[m - \033[32mSair do Sistema\033[m')
	print(20 * '--')

	a = leiaInt('Sua Opção: ')

	if a == 1:
		arqLer(arq,Titulo = 'Pessoas Cadastradas')

	elif a == 2:
		titulo('Cadastrar Nova Pessoa')
		nome = leiaNome('Nome: ')
		idade = leiaInt('Idade: ')
		cadastrar(arq, nome, idade)


	elif a == 3:
		break
	else:
		print('\033[31mOpção Inválida.\033[m')