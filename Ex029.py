v = float(input('Qual a velocidade do carro:'))
multa = 7 * (v - 80)
if v >= 80:
    print('{}Multado{}!!!!\nvocê excedeu o limite de velocidade de 80km/h'.format('\033[41m', '\033[m'))
    print('Você foi multado em R${} por ultrapassar o limite de velocidade'.format(multa))
    print('Dirige mais devagar')
else:
    print('{}Tenha um bom dia{}'.format('\033[32m','\033[m'))
    print('Você está dentro do limite de velocidade')
