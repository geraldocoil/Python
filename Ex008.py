medida = int(input('qual é a distância em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('a distância de {}m corresponde a:\n {}km kilometros\n {}hm\n {}dam\n {}dm\n {}cm\n 2e {}mm em milimetros'.format(
    medida, km, hm, dam, dm, cm, mm))
