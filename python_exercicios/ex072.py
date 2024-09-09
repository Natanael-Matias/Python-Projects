'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou {num[n]}.')
    else:
        continue
    op = input('Próximo número? [S/N] ').upper()
    while op not in 'SN':
        print('Entrada inválida!!')
        op = input('Próximo número? [S/N] ').upper()
    if op == 'N':
        print('Thanks!!!')
        break
