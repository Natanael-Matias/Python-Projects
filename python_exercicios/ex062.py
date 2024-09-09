'''Melhore o ex 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

op = False
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a = 0
s = []
while a < 10:
    s.append(n1 + a * r)
    a += 1
print(s)
a = 0
s = []
n = 10
while not op:
    b = int(input('Mostrar mais termos: '))
    n = n + b
    if b != 0:
        while a < n:
            s.append(n1 + a * r)
            a += 1
        print(s)
    else:
         op = True
         print('Fim do programa.')

