''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
 No final mostre:
 a) Total de pessoas
 b) Pessoas mais pesadas
 c) Pessoas menos pesadas'''

cad = list()
person = list()
c = 0

while True:
	person.append(input('Nome: '))
	person.append(float(input('Peso: ')))
	cad.append(person[:])
	person.clear()
	c += 1

	cont = (input('Deseja continuar?[S/N] ')).upper()
	while cont not in 'SN':
		cont = (input('Deseja continuar?[S/N] ')).upper()
	if cont == 'N':
		print('\nOs resultados são: ')
		break

n = m = cad[0][1]

for x in range(0,len(cad)):
	if cad[x][1] > m:
		m = cad[x][1]
	if cad[x][1] < n:
		n = cad[x][1]

print(f'O total de pessoas cadastradas: {c}')
print(f'As pessoas mais pesadas são:', end=' ')
for x in cad:
	if m in x:
		print('/',x[0],end=' / ')

print(f'\nAs pessoas menos pesadas são:', end=' ')
for x in cad:
	if n in x:
		print('/',x[0],end=' / ')
