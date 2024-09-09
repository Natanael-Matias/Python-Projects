def titulo(s):
	print(20 * '--')
	print(f'{s:^40}')
	print(20 * '--')


def leiaInt(s):
	while True:
		try:
			n = int(input(s))
		except (TypeError,ValueError):
			print('\033[31mErro! Opção inválida.\033[m')
		except KeyboardInterrupt:
			break
		else:
			return n
			break

def leiaNome(s):
	while True:
		a = str(input(s))
		if a.strip() == '':
			print('\033[31mEscreva o nome!\033[m')
		else:
			return a
			break

