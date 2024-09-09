''' Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(s):
	while True:
		n = str(input(s))
		if n.isnumeric():
			return int(n)
			break
		else:
			print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
