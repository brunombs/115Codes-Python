from datetime import date
maiordeidade = 0
contador = 0
menor = 0
for c in range (0, 7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - nascimento
    if idade >= 21:
        maiordeidade += 1
    else:
        menor += 1
print('{} pessoas atingiram a maioridade.'.format(maiordeidade))
print('{} pessoas não atingiram a maioridade.'.format(menor))
