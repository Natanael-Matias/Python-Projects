# ler nome e média de um aluno, guardar também a situação
# em um dicionário. Mostrar o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input('Média do aluno: '))

if aluno['Média'] >= 7:
	aluno['Situação'] = 'Aprovado'
else:
	aluno['Situação'] = 'Reprovado'

print()
#print(aluno)

print(10*'+', 'Situação do Aluno', 10*'+')

for k,v in aluno.items():
	print(f'{k}: {v}')
