d = float(input('Qual a distancia da viagem:'))
print('vc está preste a comecar uma viagem de {}Km'.format(d))
'''if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45'''
preco = d * 0.5 if d <= 200 else d * 0.45
print('O preco da sua passagem será de {}{}R${}'.format('\033[1;32m',preco,'\033[m'))
