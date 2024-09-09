# Escreva um programa que converta uma temperatura digitada
# em ºC para ºF.

C = float(input('Temperatura em ºC: '))
F = 32 + (9/5) * C
print('A temperatura em ºF: {:.2f}'.format(F))
