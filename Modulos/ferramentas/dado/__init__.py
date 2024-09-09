def leiadinheiro(a):
	while True:
		t = str(input(f'{a} ')).replace(',','.')
		t = ''.join(t.split())
		if t.isalpha() or t == '':
			print('\033[0;31mERRO! Digite um valor válido.\033[m')
		else:
			t = float(t)
			break
	return t
