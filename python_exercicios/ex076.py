'''Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequencia. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''

#print(f'{"Alojado ":·<20} 7,88') alt + 250 -> ·

compras = ('Biscoito', 4.19, 'Wafer', 1.19, 'Mortadela', 8.39, 'Arroz', 4.89)
print('#*' * 17)
print(f'#{"LISTA DE COMPRAS":^32}#')
for a in range(0, len(compras), 2):
    print(f'# \t {compras[a]:.<17} R${compras[a + 1]:>5.2f} \t #')
print('#*' * 17)
