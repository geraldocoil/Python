n = int(input('Digite um número:'))
cores={'limpa':'\033[m','verde':'\033[32m','vermelho':'\033[31m'}
n2 = n % 2
if n2 == 0:
    print('{} é um {}número par{}'.format(n,cores['verde'],cores['limpa']))
else:
    print('{} é um {}número impar{}'.format(n,cores['vermelho'],cores['limpa']))
