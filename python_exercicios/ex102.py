''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial. '''

def fatorial(a, show = False):
	"""
	Função que calcula o fatorial de um número.
	param a: número que será calculado o fatorial
	param show (opcional): se True, apresenta o calculo passo a passo
		default: False
	"""

	f = 1
	F = list()
	if a == 0:
		return f
	else:	
		for i in range(a,0,-1):
			if show:
				print(i,end=' ')
				if i > 1:
					print('x',end=' ')
				else:
					print('=',end=' ')
			f *= i
		return f

print(fatorial(5,True))