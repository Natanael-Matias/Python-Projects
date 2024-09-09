# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

dados = dict()
ano = datetime.now().date()

dados['Nome:'] = str(input('Digite seu nome: '))

nascimento = str(input('Data de nascimento: '))
ano_nas = int(nascimento[6:])
born = datetime.strptime(nascimento, '%d %m %Y').date()
idade = relativedelta(ano, born)
dados['Idade:'] = idade.years
dados['CTPS:'] = int(input('Número da carteira de trabalho (0: não tem.): '))

if dados['CTPS:'] != 0:
	dados['Contratação:'] = int(input('Ano de contratação: '))
	dados['Salário:'] = int(input('Salário: '))
	dados['Aposentadoria:'] = dados['Contratação:'] - ano_nas + 35
	print('+-+'*15)
	for k,v in dados.items():
		print(f'{k} {v}')

else:	
	print('+-+'*15)
	for k,v in dados.items():
		print(f'{k} {v}')
