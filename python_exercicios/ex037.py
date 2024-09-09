'''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
1 -> binário
2 -> octal
3 -> hexadecimal'''

n = int(input('digite um número: '))
print('Escolha uma das bases para conversão:')
print('[1] - Para converter para binário.')
print('[2] - Para converter para octal.')
print('[3] - Para converter para hexadecimal.')
e = int(input('Sua opção: '))

if e == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif e == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif e == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
