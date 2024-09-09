''' Crie um programa que leia o nome completo de uma pessoa e mostre:
 -> O nome com todas as letras maiúsculas.
 -> O nome com todas as letras minúsculas.
 -> Quantas letras no total (sem considerar espaços).
 -> Quantas letras tem o primeiro nome. '''

name = input('Type your name: ')
print(name.upper())
print(name.lower())
sp = name.split()
ts = ''.join(sp)
print('O nome todo possui {} letras'.format(len(ts)))
print('O primeiro nome possui {} letras'.format(len(sp[0])))
