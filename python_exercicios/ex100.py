''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.'''

def sorteia(N):
	from random import randint
	from time import sleep

	print('Sorteando 5 valores: ',end='')
	for x in range(0,5):
		N.append(randint(0,10))
		print(f'{N[x]}',end=' ')
		sleep(0.3)


def somaPar(N):
	S = 0
	for x in N:
		if x%2 == 0:
			S += x
	print(f'\nA soma dos valores pares em {N} é: {S}')


Num = list()
sorteia(Num)
somaPar(Num)
