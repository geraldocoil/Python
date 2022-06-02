s=int(input('Qual é o seu sálario R$:'))
cores={'limpa':'\033[m','verde':'\033[32m'}
if s>1250:
    #a=s*0.1
    a=s*10/100
    print('O seu aumento será de {}R${:.1f}{}'.format(cores['verde'],a,cores['limpa']))
    print('Seu novo sálario será de {}R${:.1f}{}'.format(cores['verde'],s+a,cores['limpa']))
else:
    #a2=s*0.15
    a2=s*15/100
    print('O seu aumento será de {}R${:.1f}{}'.format(cores['verde'],a2,cores['limpa']))
    print('Seu novo sálario será de {}R${:.1f}{}'.format(cores['verde'],s+a2,cores['limpa']))

print('Meus parabéns, continue com seu ótimo trabalho!!')
