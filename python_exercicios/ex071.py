'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte ao usuário qual valor será sacado e programa irá informar
quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.'''

while True:
    n = [0, 0, 0]
    valor = int(input('Digite o valor a ser sacado: R$'))
    if valor // 50 >= 1:
        n[0] = valor // 50
        valor -= 50 * n[0]
    if valor // 20 >= 1:
        n[1] = valor // 20
        valor -= 20 * n[1]
    if valor // 10 >= 1:
        n[2] = valor // 10
        valor -= 10 * n[2]

    print('Serão sacadas:')
    if n[0] > 0:
        print(f'{n[0]} nota(s) de R$50,00.')
    if n[1] > 0:
        print(f'{n[1]} nota(s) de R$20,00.')
    if n[2] > 0:
        print(f'{n[2]} nota(s) de R$10,00.')
    if valor > 0:
        print(f'{valor} nota(s) de R$1,00.')

    op = input('Deseja sacar mais: [S/N] ').strip().upper()
    while op not in 'SN' or op == '':
        print('Entrada Inválida!!!')
        op = input('Deseja sacar mais: [S/N] ').strip().upper()
    if op == 'N':
        print('\nVolte Sempre.')
        break
