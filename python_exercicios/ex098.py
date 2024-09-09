'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada.
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador(i,f,p):
	from time import sleep

	if p == 0:
		print('ERRO!')
	else:
		if i <= f:
			pos = i
			print(15 * '-=')
			while pos <= f:
				print(f'{pos}',end=' ')
				pos += abs(p)
				sleep(0.5)
			print('FIM!')
		elif i > f:
			pos = i
			print(15 * '-=')
			while pos >= f:
				print(f'{pos}',end=' ')
				pos -= abs(p)
				sleep(0.5)
			print('FIM!')


contador(1,10,1)
contador(10,0,2)

print(15 * '-=')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)