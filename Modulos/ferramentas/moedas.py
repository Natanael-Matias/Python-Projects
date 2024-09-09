def moeda(valor):
	v = f'{valor:.2f}'
	v = str(v)
	return f'R${v[:-3]},{v[-2:]}'


def aumentar(valor, acres):
	"""
	param valor: valor a ser modificado
	param acres: quantidade em % que será acrescentado
	"""

	v = valor*(1+acres/100)
	return moeda(v)


def diminuir(valor, dim):
	"""
	param valor: valor a ser modificado
	param dim: quantidade em % que será diminuido
	"""

	v = valor*(1-dim/100)
	return moeda(v)


def dobro(valor):
	v = 2*valor
	return moeda(v)


def metade(valor):
	v = valor/2
	return moeda(v)


def resumo(v, aum = 0, dim = 0):
	print(40 * '-')
	print(f'{"RESUMO DO VALOR":^40}')
	print(40 * '-')

	print(f'Preço analisado: \t {moeda(v)}')
	print(f'Dobro do preço: \t {dobro(v)}')
	print(f'Metade do preço: \t {metade(v)}')
	print(f'{aum}% de aumento: \t {aumentar(v,aum)}')
	print(f'{dim}% de desconto: \t {diminuir(v,dim)}')
	print(40 * '-')