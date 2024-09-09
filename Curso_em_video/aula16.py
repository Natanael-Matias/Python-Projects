'''Tuplas: variáveis compostas inicializadas por () ou sem nada.
Tuplas são IMUTÁVEIS! Não é possível modificar '''

#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

strings = []
pontos = []
inteiros = []
var = 'nada', 65, 'oi', 3.4, 'tudo'

for c in range(len(var)):
    if type(var[c]) == str:
        strings.append(var[c])
        
    elif type(var[c]) == int:
        inteiros.append(var[c])
        
    elif type(var[c]) == float:
        pontos.append(var[c])

print(f'''{strings}
{inteiros}
{pontos}''')

strings = []
pontos = []
inteiros = []

for pos, element in enumerate(var):     #
    if type(element) == str:            #
        strings.append(var[pos])        #
                                        #
    elif type(element) == int:          # element -> objeto que está na tupla.
        inteiros.append(var[pos])       # pos -> posição do objeto. Semelhante à
                                        #   for pos in range(0, len(var))
    elif type(element) == float:        #
        pontos.append(var[pos])         #
                                        #
print(f'''{strings}
{inteiros}                              
{pontos}''')

# Ambos os códigos acima fazem exatamente a mesma coisa!