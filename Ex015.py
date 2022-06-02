dias = int(input('quantidade de dias alugados:'))
km = float(input('kilometros rodados:'))
p = dias * 60 + 0.15 * km
print('o carro foi alugado por {} dias e percor10reu {}Km'.format(dias, km))
print('o valor a ser pago será de R${:.2f}'.format(p))
