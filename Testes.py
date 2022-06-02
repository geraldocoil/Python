nome=str(input('Digite seu nome:')).strip().capitalize()
print('Seu nome tem {} letras'.format(len(nome)-len(' ')))
print('O seu nome tem {} a(s)'.format(nome.count('a')))
