'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos'''

d = 0
h = 0
m = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').upper()
    if sexo not in 'MF' or sexo == '':
        print('Entrada Inválida!!!')
        continue
    else:
        if idade > 18:
            d += 1
        if sexo == 'M':
            h += 1
        if sexo == 'F' and idade < 20:
            m += 1

    op = input('Dejesa cadastrar mais alguém [S/N]? ').upper()
    while op not in 'SN' or op == '':
        print('Entrada Inválida!!!')
        op = input('Dejesa cadastrar mais alguém [S/N]? ').upper()
    if op == 'N':
        break

print(f'{d} pessoas tem mais de 18 anos.')
print(f'{h} homens foram cadastrados.')
print(f'{m} mulheres tem menos de 20 anos.')
