print('{} Analisador de Triângulos {}'.format('-=-' * 10, '-=-' * 10))
cores={'limpa':'\033[m','verde':'\033[32m','vermelho':'\033[31m'}
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite um último número:'))
# if abs(n2 - n3) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com os lados {}cm,{}cm e {}cm {} É POSSÍVEL FORMAR UM TRIÂNGULO{}!!!!'.format(n1, n2, n3,cores['verde'],cores['limpa']))
else:
    print('{}Não é possivel montar um triângulo com esses lados{}!!!'.format(cores['vermelho'],cores['limpa']))
if n1 == n2 == n3:
    print('O triângulo formado é equilatero')
