'''Crie um programa qe vai ler vários números e colocar e uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenados de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''

c = 0
v = list()
while True:
    n = int(input('Digite um número: '))
    if n == 5:
        c += 1
    v.append(n)

    op = input('Deseja continuar: [S/N] ').upper()
    while op not in 'SN':
        op = input('Deseja continuar: [S/N] ').upper()
    if op == 'N':
        break
v.sort(reverse=True)

print(f'\nForam digitados {len(v)} valores.')
print(f'Em ordem decrescente: {v}')
print(f'O número 5 está na lista e foi digitado {c} vezes' if 5 in v else
      'O número 5 não foi digitado.')
