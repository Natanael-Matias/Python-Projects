'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta'''

pa = 0
pf = 0
v = input('Digite uma frase: ').split()

for a in v:
    for c in range(len(a)):
        if a[c] == '(':
            pa += 1
        if a[c] == ')':
            pf += 1
        if pf > pa:
            print('ERRO!!!')
            break
    if pf > pa:
        break

if pa == pf == 0:
    print('Não houveram parênteses.')
elif pa == pf > 0:
    print('Parênteses finalizados corretamente.')
elif pa > pf:
    print('ERRO!!!')
