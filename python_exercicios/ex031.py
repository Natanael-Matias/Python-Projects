'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cabrando R$0,50/km para viagens de até 200 km e
R$0,45/km para viagens mais longas'''

d = float(input('Digite a distância de sua viagem em km: '))
if d <= 200:
    print('O valor da passagem será R${:.1f}'.format(d * 0.50))
else:
    print('O valor da viagem será R${:.1f}'.format(d * 0.45))
