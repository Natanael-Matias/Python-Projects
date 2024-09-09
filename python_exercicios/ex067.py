'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número for negativo.'''

while True:
    print('-*' * 10)
    print(f'{"TABUADA":^20}')
    print('-*' * 10)
    n = int(input('Digite um valor: '))
    if n < 0:
        print('Fim do Programa.')
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
