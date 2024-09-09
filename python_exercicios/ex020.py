''' O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

import random
n1 = input('aluno: ')
n2 = input('aluno: ')
n3 = input('aluno: ')
n4 = input('aluno: ')
list = [n1, n2, n3, n4]
random.shuffle(list)

print('A ordem será: {}'.format(list))
#print(list)
