'''Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Não existe valor maior, ambos são iguais.'''

a = int(input('Digite um número: '))
b = int(input('Digite mais um: '))

if a > b:
    print('O primeiro é maior!')
elif b > a:
    print('O segundo é maior!')
else:
    print('Os números são iguais!')
