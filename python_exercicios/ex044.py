'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
- à vista no dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

v = float(input('Digite o valor da compra: R$ '))
print('\033[7;30;41m1 - à vista no dinheiro/cheque.\033[m')
print('\033[7;30;41m2 - à vista no cartão.', '\033[7;30;41m \033[m' * 8)
print('\033[7;30;41m3 - em até 2x no cartão.', '\033[7;30;41m \033[m' * 6)
print('\033[7;30;41m4 - 3x ou mais no cartão.', '\033[7;30;41m \033[m' * 5)
e = int(input('Escolha a forma de pagamento: '))

if e == 1:
    print('O valor final do produto séra R${:.2f}.'.format(v * 0.9))
elif e == 2:
    print('O valor final do produto séra R${:.2f}.'.format(v * 0.95))
elif e == 3:
    print('Serão 2 (duas) parcelas de R${:.2f}.'.format(v / 2))
elif e == 4:
    p = int(input('Quantidade de parcelas: '))
    print('O valor da compra foi dividido em {} parcelas de R${:.2f}.'.format(p, (v * 1.2)/p))
