'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
op = False
while not op:
    print('==-==' * 6)
    print('''\t[1] somar
\t[2] multiplicar
\t[3] maior
\t[4] novos números
\t[5] sair do programa''')
    print('==-==' * 6)
    o = int(input('Escolha uma das opções: '))
    if o == 1:
        print('A soma entre {} e {} será: {}\n'.format(n1, n2, n1 + n2))
    elif o == 2:
        print('O produto entre {} e {} será: {}\n'.format(n1, n2, n1 * n2))
    elif o == 3:
        if n1 > n2:
            print('O maior valor é {}.\n'.format(n1))
        else:
            print('O maior valor é {}.\n'.format(n2))
    elif o == 4:
        print('Digite novos números:')
        n1 = int(input('Pri. Número: '))
        n2 = int(input('Seg. Número: '))
    elif o == 5:
        print('Fim do Programa.')
        op = True
    else:
        print('Opção inválida. Tente novamente.\n')
