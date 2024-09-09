'''Crie um programa que tenha uma tupla com várias palavras (sem acentos)
Depois disso, você deverá mostrar, para cada palavra, quais são suas vogais.'''

palavras = ('inospito', 'datilografo', 'filha', 'enjoada', 'chorona')
for p in palavras:
    print(f'A palavra "{p}" possui as vogais: ', end='')
    for c in range(len(p)):
        if p[c] in 'aeiou':
            print(p[c], end='')
    print('\n')
