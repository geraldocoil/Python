import math

co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
# h=math.sqrt(math.pow(co,2)+math.pow(ca,2))
h = math.hypot(co, ca)
# h=(co**2+ca**2)**(1/2)
print('a hipotenusa vai medir {:.2f}cm'.format(h))
