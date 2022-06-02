l = float(input(" largura da parede:"))
h = float(input(' altura da parede:'))
a = l * h
print('A parede possui as dimensoes de {}m*{}m e possui {:.3f}m^2 de área'.format(l,h,a))
print('Serão necessários {:.1f}L de tinta para pintar a parede'.format(a / 2))
