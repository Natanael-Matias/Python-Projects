'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável. '''

def escreva(txt):
	l = len(txt) + 4
	print(l*'~')
	print(f'  {txt}')
	print(l*'~')


#titulo = str(input('Digite o título: '))
#escreva(titulo)
