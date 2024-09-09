import urllib
import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
	print('Não é possível acessar.')
else:
	print('É possível acessar.')


