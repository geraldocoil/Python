from time import sleep
nome = str(input('Digite o seu nome completo:')).strip().title()
print('Analisando seu nome...')
sleep(2)
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Ao todo o seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
d=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(d[0],len(d[0])))
