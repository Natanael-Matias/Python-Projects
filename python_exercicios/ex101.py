''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(s):
	from datetime import datetime,timedelta
	from dateutil.relativedelta import relativedelta

	anoatual = datetime.now().date()
	nascimento = datetime.strptime(s, '%d %m %Y').date()

	idade = relativedelta(anoatual,nascimento).years

	if idade > 17 and idade < 60:
		print(f'Pessoa com {idade} anos. Voto Obrigatório!')
	elif idade > 15 and idade < 18 or idade > 60:
		print(f'Pessoa com {idade} anos. Voto Opcional!')
	else:
		print(f'Pessoa com {idade} anos. Não Vota!')


born = str(input('Data de Nascimento: '))
voto(born)
