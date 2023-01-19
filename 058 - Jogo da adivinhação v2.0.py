from random import randint
numerocomputador = randint(0, 10)
c = 0
palpite = int(input('O computador selecionou um número entre 0 e 10, tente adivinhar qual foi esse número: '))
while palpite != numerocomputador:
    if numerocomputador > palpite:
        print('Dica: é um número superior ao que você selecionou')
    elif numerocomputador < palpite:
        print('Dica: é um número inferior ao que você selecionou')
    palpite = int(input('Infelizmente você não acertou, tente novamente: '))
    c += 1
print('Parabéns, você acertou! O computador pensou no número {} e você precisou de {} tentativa(s) até adivinhar :)'.format(numerocomputador, c))
