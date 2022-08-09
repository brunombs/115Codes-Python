from datetime import date
anodenascimento = int(input('Digite o ano em que você nasceu: '))
anoatual = date.today().year
idade = anoatual - anodenascimento
idadealistamento = anodenascimento + 18
idadeexcedente = anoatual - idadealistamento
idaderestante = idadealistamento -anoatual

if anoatual < idadealistamento:
    print('Quem nasceu em {} tem ou terá {} anos em {}'.format(anodenascimento, idade, anoatual))
    print('Você  ainda vai se alistar, falta(m) {} ano(s)'.format(idaderestante))
elif anoatual == idadealistamento:
    print('Quem nasceu em {} tem ou terá {} anos em {}'.format(anodenascimento, idade, anoatual))
    print('Já está na hora de você se alistar')
elif anoatual > idadealistamento:
    print('Quem nasceu em {} tem ou terá {} anos em {}'.format(anodenascimento, idade, anoatual))
    print('Já passou da hora de você se alistar há {} ano(s)'.format(idadeexcedente))
