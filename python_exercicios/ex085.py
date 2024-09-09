'''Digitar 7 valores numéricos e guardá-los em uma lista que separe-os entre ímpares e pares.
No final mostre os valores pares e ímpares em ordem crescente.'''

number = [[],[]]
for x in range(0,7):
	n = int(input(f'Digite o {x+1}º valor: '))
	if n % 2 == 0:
		number[0].append(n)
	else:
		number[1].append(n)

number[0].sort()
number[1].sort()


print(15*'-=',f'\nOs números pares são: {number[0]}\nOs números ímpares são: {number[1]}')