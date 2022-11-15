from datetime import datetime
anoatual = datetime.today().year
def voto(num):
    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos o VOTO É OBRIGATÓRIO!')
    if idade >= 16 and idade < 18:
        print(f' Com {idade} anos o VOTO É OPCIONAL!')
    if idade < 16:
        print(f' Com {idade} anos o VOTO É NEGADO!')


anodenascimento = int(input('Digite o ano de seu nascimento: '))
idade = anoatual - anodenascimento
voto(idade)