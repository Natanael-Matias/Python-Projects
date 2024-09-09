'''Ler nome e duas notas de vários alunos, mostrar um boletim com a média de cada
aluno e permita que o usuário possa mostrar as notas de cada um individualmente.'''

turma = list()
nota = list()
aluno = list()
media = 0

while True:
	nome = str(input('Nome do aluno: ')).capitalize()
	for x in range(0,2):
		nota.append(float(input(f'{x+1}ª nota: ')))
		media += nota[x]

	aluno.append(nome[:])
	aluno.append(nota[:])
	aluno.append(media/2)
	nota.clear()
	media = 0
	turma.append(aluno[:])
	aluno.clear()

	op = input('Deseja continuar? [S/N] ').upper()
	while op not in 'SN':
		op = input('Deseja continuar? [S/N] ').upper()
	if op == 'N':
		break

print(5*'-=', '>BOLETIM<', 5*'-=')
print(f'{"NOME":<15} MÉDIA')
print(30*'-')


for x in turma:
	print(f'{x[0]:<15} {x[2]}')
print(15*'-=')

for x in turma:
	aluno.append(x[0])
	aluno.append(x[1])

op = str(input('Mostrar notas("Não" encerra): ')).capitalize()

while True:
	while op not in aluno:
		print('Nome inválido!!')
		op = str(input('Mostrar notas: ')).capitalize()
		if op == 'Não':
			break

	if op in aluno:
		print(f'As notas de {op} são', end=' ')
		for x,l in enumerate(turma):
			if l[0] == op:
				print(l[1])
		op = str(input('Mostrar notas: ')).capitalize()
	if op == 'Não':
		print('FIM DO PROGRAMA!')
		break
