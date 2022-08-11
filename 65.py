número = int(input('Digite um número: '))
resposta = str(input('Quer continuar? [S/N] ')).upper()
soma = 0
primeironúmero = número
contador = 1
maiornúmero = número
menornúmero = número
while resposta != ('N'):
    número = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    soma += número
    contador += 1
    if número > maiornúmero:
        maiornúmero = número
    if número < menornúmero:
        menornúmero = número
if resposta == ('N'):
    print('A média dos valores que você digitou é: {:.2f}'.format((primeironúmero + soma) / contador))
    print('O maior número que você digitou foi {}'.format(maiornúmero))
    print('O menor número que você digitou foi {}'.format(menornúmero))