anodenascimento = int(input('Digite o ano em que você nasceu: '))
anoatual = 2022
idadealistamento = anodenascimento + 18
idadeexcedente = anoatual - idadealistamento
idaderestante = idadealistamento -anoatual

if 2022 < idadealistamento:
    print('Você  ainda vai se alistar, falta(m) {} ano(s)'.format(idaderestante))
elif 2022 == idadealistamento:
    print('Já está na hora de você se alistar')
elif 2022 > idadealistamento:
    print('Já passou da hora de você se alistar há {} ano(s)'.format(idadeexcedente))
