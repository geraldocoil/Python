from datetime import date
ano=int(input('Em que ano estamos? :'))
if ano==0:
    ano=date.today().year
if ano %4==0 and ano%100 !=0 or ano%400==0:
    print('{} é um ano {}BISSEXTO'.format(ano,'\033[34m'))
else:
    print('{} é um {}ANO NORMAL'.format(ano,'\033[33m'))
