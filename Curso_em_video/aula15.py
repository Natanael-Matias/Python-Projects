'''Interrompendo repetições while'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # <- Sai do laço.
    s += n
print(f'A soma vale {s}.')
