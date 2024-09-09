'''Faça a tabuada de um número que o usuário escolher.'''

n = int(input('Digite um número entre 1 e 10: '))
print('A tabuada do {} é:'.format(n))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n * c)))
