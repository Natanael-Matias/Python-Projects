''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional) '''

def notas(*n, sit = False):
	maior = n[0]
	menor = n[0]
	media = 0
	aluno = dict()

	for i in n:
		if i > maior:
			maior = i
		if i < menor:
			menor = i
		media += i

	media = media/len(n)

	aluno['Quantidade'] = len(n)
	aluno['Maior'] = maior
	aluno['Menor'] = menor
	aluno['Média'] = media

	if sit:
		if media < 5:
			aluno['Situação'] = 'Insuficiente'
		elif media < 7:
			aluno['Situação'] = 'Regular'
		elif media < 9:
			aluno['Situação'] = 'Bom'
		else:
			aluno['Situação'] = 'Excelente'

	return aluno


resp = notas(5.5,2.5,10,6.5,sit=True)
print(resp)
