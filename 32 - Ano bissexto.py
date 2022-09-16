from datetime import date
ano = int(input('Digite o ano para saber se ele é ou não bissexto: '))
if ano == 0:
    ano = date.today().year
    print('Você digitou zero, recalculamos para o ano atual e vimos que em {}:'.format(ano))
if ano % 4 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
