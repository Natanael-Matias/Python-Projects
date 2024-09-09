''' Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''

name = input('Type your complete name: ').strip()
n1 = name.find(' ')
n2 = name.rfind(' ')
print('Nice to meet you!!!')
print('Your first name is: {}'.format(name[:n1].capitalize()))
print('Your last name is: {}'.format(name[n2 + 1:].capitalize()))
