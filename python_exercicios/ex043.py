'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status
- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 a 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida.'''

print('\033[7;30m*=\033[m' * 15)
print('\033[7;30;41mÍndice de Massa Corporal - IMC\033[m')
print('\033[7;30m*=\033[m' * 15)
m = float(input('Digite sua massa em kg: '))
h = float(input('Digite sua altura em metros: '))
imc = m / (h ** 2)

if imc <= 18.5:
    print('Seu IMC é {:.1f} e você está com baixo peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.1f} e você está com o peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida.'.format(imc))
