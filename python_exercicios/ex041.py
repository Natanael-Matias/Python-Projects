'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SÊNIOR
- acima: MASTER'''

from datetime import date
atual = date.today().year
nas = int(input('Digite o ano de nascimento do atleta: '))
idd = atual - nas

if idd <= 9:
    print('Sua idade é {} anos, portanto sua categoria é MIRIM.'.format(idd))
elif idd <= 14:
    print('Sua idade é {} anos, portanto sua categoria é INFANTIL.'.format(idd))
elif idd <=19:
    print('Sua idade é {} anos, portanto sua categoria é JUNIOR.'.format(idd))
elif idd <= 25:
    print('Sua idade é {} anos, portanto sua categoria é SÊNIOR.'.format(idd))
else:
    print('Sua idade é {} anos, portanto sua categoria é MASTER.'.format(idd))
