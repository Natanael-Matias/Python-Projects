''' Faça um programa que leia uma frase pelo teclado e mostre:
 -> Quantas vezes aparece a letra "A".
 -> Em que posição ela aparece a primeira vez.
 -> Em que posição ela aparece a última vez. '''

phrase = input('Type a phrase: ').lower().strip()
print('The letter \'A\' appears {} times.'.format(phrase.count('a')))
print('The first position is: {}'.format(phrase.find('a') + 1))
print('The last position is: {}'.format(phrase.rfind('a') + 1))
