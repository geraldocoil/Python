frase=str(input('Digite algo:')).lower().strip()
#frase=frase.lower().strip()
print('a letra (a) aparece {} vezes'.format(frase.count('a')))
print('ele aparece pela primeira vez no caracter {}'.format(frase.find('a')+1))
print('ele aparece pela ultima vez no caracter {}'.format(frase.rfind('a')+1))
