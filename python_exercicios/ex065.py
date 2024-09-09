'''Crie um programa que leia vários números inteiros pelo teclado. No final,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

s = 0
maior = menor = 0
l = []
n = int(input('Digite um número: '))
l.append(n)
op = input('Deseja digitar outro valor? [Y/N]: ').upper()
while op not in 'N':
    if op == 'Y':
        n = int(input('Digite um número: '))
        op = input('Deseja digitar outro valor? [Y/N]: ').upper()
        l.append(n)
    else:
        print('Entrada inválida!!')
        op = input('Deseja digitar outro valor? [Y/N]: ').upper()
a = 0
while a < len(l):
    s += l[a]
    if a == 0:
        maior = l[a]
        menor = l[a]
    else:
        if l[a] > maior:
            maior = l[a]
        if l[a] < menor:
            menor = l[a]
    a += 1

print('''A média é: {:.2f} 
O maior é: {}
O menor é: {}'''.format(s / len(l), maior, menor))
