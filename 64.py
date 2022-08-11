contador = 0
soma = 0
número = int(input('Digite um número: '))
primeironúmero = número
while número != 999:
    print('Você selecionou o número {}, digite outro e tente descobrir qual o número que irá parar o programa.'.format(número))
    número = int(input('Digite outro número: '))
    contador += 1
    soma += número
print('Você precisou de {} tentativas até adivinhar que o número que para o programa é {}'.format(contador, número))
print('A soma dos números que você digitou até chegar ao {} e desconsiderando o {} foi: {}'.format(número, número, soma + primeironúmero - 999))