from datetime import date
anodenascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - anodenascimento
print('O atleta tem {}'.format(idade))
if idade < 10:
    print('A categoria é: MIRIM')
elif idade >= 10 and idade <= 14:
    print('A categoria é: INFANTIL')
elif idade > 14 and idade < 20:
    print('A categoria é: JUNIOR')
elif idade == 20:
    print('A categoria é: SÊNIOR')
elif idade > 20:
    print('A categoria é: MASTER')