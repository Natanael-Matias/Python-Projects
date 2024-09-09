from Modulos.interface import *

def arqExiste(nome):
	try:
		a = open(nome, 'rt')
		a.close()
	except FileNotFoundError:
		return False
	else:
		return True


def arqCriar(nome):
	try:
		a = open(nome, 'wt+')
		a.close()
	except:
		print(f'\033[31mHouve um erro ao criar o arquivo {nome}.\033[m')
	else:
		pass


def arqLer(nome,Titulo = 'Nada'):
	try:
		a = open(nome, 'rt')
	except:
		print('\033[31mErro ao ler o arquivo.\033[m')
	else:
		titulo(Titulo)
		print(a.read())
	finally:
		a.close()


def cadastrar(arq, nome, idade = 0):
	try:
		a = open(arq, 'at')
	except:
		print('\033[31mHouve um ERRO ao abrir o arquivo.\033[m')
	else:
		try:	
			a.write(f'{nome:<30}  {idade} anos\n')
		except:
			print('\033[31mHouve um ERRO no cadastro\033[m')
		else:
			print('\033[34mNovo Cadastro Realizado com Sucesso.\033[m')
			a.close()

