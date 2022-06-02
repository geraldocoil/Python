from math import radians,sin,cos,tan
a=float(input('valor do angulo:'))

sen=sin(radians(a))
cos=cos(radians(a))
tg=tan(radians(a))
print('para o angulo de {} graus\n o SENO vale {:.2f}\n o COSSENO vale {:.2f}\n e a TANGENTE vale {:.2f}'.format(a,sen,cos,tg))

