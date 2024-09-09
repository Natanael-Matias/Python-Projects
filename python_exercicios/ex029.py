''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/m,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 para cada
 km acima do limite.'''

v = float(input('Escreva a volocidade do veículo: '))
if v > 80.0:
    print('Você foi multado em R${:.2f}, pois estava acima do permitido'.format((v - 80) * 7.0))
    print('SEJA MAIS RESPONSÁVEL!')
else:
    print('Faça uma boa viagem!')