''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
o nome do escolhido '''

from random import choice
alunos = ['Ana', 'Lohan', 'Laura', 'Bento', 'Erick', 'Ricco', 'Arthur']
esq = choice(alunos)

print('O escolhido foi: {}'.format(esq))
