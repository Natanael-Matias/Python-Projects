''' Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com a palavra "SANTO" '''

name = input('Enter the city name: ')
n1 = name.lower().split()
print('Does the city name start with "Santo"? {}'.format('santo' in n1[0]))
