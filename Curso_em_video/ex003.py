n = input('Digite algo: ')
print(type(n))
print('é alfanumérico? ', n.isalnum())
print('é letra? ', n.isalpha())
print('é um número? ', n.isnumeric())
print('Possui apenas espaços? ', n.isspace())
print(n.isdecimal())
