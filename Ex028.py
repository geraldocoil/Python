import random
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=-'*20)
n1 = random.randint(0, 5)
n2 = int(input('Em que número eu pensei?:'))
print('PROCESSANDO....')
sleep(1)
if n1 == n2:
    print('{}Parabens vc acertou!!!!!!!!!!!{}'.upper().format('\033[32m','\033[m'))
    print('o número era {}'.format(n2))
else:
    print('{}infelismente vc errou, o computador ganhou{}'.upper().format('\033[31m','\033[m'))
    print('o número era {}'.format(n1))
