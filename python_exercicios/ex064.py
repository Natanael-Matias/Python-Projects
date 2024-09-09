'''Crie um programa que leia varios numeros interios pelo teclado. O programa
vai para quando o usuário digitar 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles. Desconsiderando o 999.'''

n = int(input('Digite um número: '))
s = 0
while n != 999:
    s += n
    n = int(input('Digite outro número [999 para encerrar]: '))
print('A soma dos números digitados é:', s)
