a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
c = int(input('Digite um ultimo número:'))
cores={'limpa':'\033[m','vermelha':'\033[31m','verde':'\033[32m'}
# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}{}{}'.format(cores['verde'],maior,cores['limpa']))
print('O menor valor digitado foi {}{}{}'.format(cores['vermelha'],menor,cores['limpa']))

