'''Escreva um programa que pergunte o salário de funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%. Para inferiores ou iguais
o aumento é de 15%.'''

s = float(input('Salário: R$'))
if s <= 1250:
    print('Seu novo salário será: R${:.1f}'.format(s * 1.15))
else:
    print('Seu novo salário será: R${:.1f}'.format(s * 1.1))
