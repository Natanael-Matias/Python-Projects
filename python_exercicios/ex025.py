''' Crie um programa que leia o nome de uma pessoa e
 diga se ela tem "Silva" no nome.'''

name = input('Type your complete name: ').lower()
print('Does your name have \'Silva\'?: {}'.format('silva' in name))
