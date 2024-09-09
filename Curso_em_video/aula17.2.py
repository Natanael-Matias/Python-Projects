'''Listas (Parte 2)'''
#Listas Compostas
'''teste = list()
teste.append('Natanael')
teste.append(27)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste)
print(galera)'''
# O código acima está incorreto pois, em Python, a = b gera uma ligação entre a e b.
# É necessário fazer uma cópia, como mostrado abaixo.

teste = list()
teste.append('Natanael')
teste.append(27)
galera = list()
galera.append(teste[:]) # Gera ma cópia de teste em galera.
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste[:])
print(galera)

# Assim é possível navegar nas listas dentro das listas
print(galera[1][0])
print(galera[0])
print(galera[0][1])
