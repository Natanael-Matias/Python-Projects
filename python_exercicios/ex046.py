'''Faça um programa que mostre na tela uma contagem regressiva
indo de 0 até 10, com uma pausa de 1 segundo entre eles.'''

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
