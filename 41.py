anodenascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2022 - anodenascimento

if idade < 10:
    print('A sua categoria é: MIRIM')
elif idade >= 10 and idade <= 14:
    print('A sua categoria é: INFANTIL')
elif idade > 14 and idade < 20:
    print('A sua categoria é: JUNIOR')
elif idade == 20:
    print('A sua categoria é: SÊNIOR')
elif idade > 20:
    print('A sua categoria é: MASTER')