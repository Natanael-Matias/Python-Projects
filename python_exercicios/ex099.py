'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
	from time import sleep

	M = 0
	c = 0
	while c < len(num):
		if c == 0:
			M = num[c]
		else: 
			if num[c] > M:
				M = num[c]
		c += 1

	print('-='*30)
	print('Analisando os valores passados...')
	for i in range(0,len(num)):
		print(f'{num[i]}',end=' ')
		sleep(0.5)
	print(f'Foram informados {len(num)} valores ao todo.')
	print(f'O maior valor informado foi {M}.')

maior(-2,-9,-4,-5,-7,-1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
