''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média '''

cadastro = dict()
pessoas = list()
F = list()
AM = list()
somaidade = 0

while True:
	cadastro['Nome'] = str(input('Nome: '))
	
	cadastro['Sexo'] = str(input('Sexo: ')).upper()
	while cadastro['Sexo'] not in 'MF':
		print('ERRO! Digite M ou F')
		cadastro['Sexo'] = str(input('Sexo: ')).upper()
	
	cadastro['Idade'] = int(input('Idade: '))
	somaidade = somaidade + cadastro['Idade']
	
	pessoas.append(cadastro.copy())
	
	Continue = str(input('Deseja continuar? [S/N] '))
	while Continue not in 'SsNn':
		print('ERRO! Digite S ou N')
		Continue = str(input('Deseja continuar? [S/N] '))
	if Continue in 'Nn':
		print('Cadastramento Encerrado.')
		break

Media = somaidade/len(pessoas)

for i in range(0,len(pessoas)):
	if pessoas[i]['Idade'] > Media:
		AM.append(pessoas[i])
	if pessoas[i]['Sexo'] in 'F':
		F.append(pessoas[i])

print('*',end='')
print(30*'-*')

print(f'A) {len(pessoas)} pessoas cadastradas.')

print(f'B) Média das idades: {Media} anos.')

print(f'C) As mulheres cadastradas foram:')
for i in range(0,len(F)):
	for k,v in F[i].items():
		print(f'	{k}: {v}.',end=' ')
	print()

print(f'D) As pessoas com idade acima da média são:')
for i in range(0,len(AM)):
	for k,v in AM[i].items():
		print(f'	{k}: {v}.',end=' ')
	print()