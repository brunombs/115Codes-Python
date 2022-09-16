distancia = int(input('Digite a distância em kms da sua casa até um destino que você quer conhecer: '))
if distancia < 200:
    passagem = distancia * 2.50
    print('O valor da passagem é: {} reais'.format(passagem))
else:
    passagem = distancia * 2.10
    print('O valor da passagem é: {} reais'.format(passagem))
