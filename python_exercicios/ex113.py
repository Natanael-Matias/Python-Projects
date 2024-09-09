''' Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(s):
	while True:
		try:
			n = int(input(s))
		except KeyboardInterrupt:
			print('\033[0;35mPrograma Finalizado.\033[m')
			break
		except:
			print('\033[0;31mERRO! Digite um número INTEIRO válido.\033[m')
		else:
			return n
			break


def leiaFloat(s):
	while True:
		try:
			f = float(input(s))
		except KeyboardInterrupt:
			print('\033[0;35mPrograma Finalizado.\033[m')
			break
		except:
			print('\033[31mERRO! Digite um número REAL válido.\033[m')
		else:
			return f
			break



n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')

print(f'O valor inteiro foi {n1} e valor real foi {n2}.')