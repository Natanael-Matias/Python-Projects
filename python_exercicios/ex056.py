'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final de programa
mostre: A media de idade do grupo
Qual o nome do homem mais velho
quantas mulheres têm menos de 20 anos.'''

md = 0
hmv = ''
imv = 0
nm = 0

for c in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c)).capitalize()
    idd = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = input('Digite o sexo da {}ª pessoa: '.format(c)).lower()
    md += idd
    if sexo == 'm' and idd > imv:
        imv = idd
        hmv = nome
    if sexo == 'f' and idd < 20:
        nm += 1
    print('\n')
print('A média de idade é {:.2f} anos.'.format(md / 4))
print('O nome do homem mais velho é {} e tem {} anos.'.format(hmv, imv))
print('{} mulheres possuem idade abaixo de 20 anos.'.format(nm))
