'''Escreva um programa para aprovar um empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo
será negado.'''

v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o salário: R$'))
t = int(input('Tempo de pagamento em anos: '))
p = v / (t * 12)

if p <= (0.3 * s):
    print('Seu financiamento foi APROVADO \nAs parcelas serão de R${:.2f}'.format(p))
else:
    print('Seu financiamento foi NEGADO.')
