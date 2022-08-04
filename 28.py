from random import randint

numero = randint(0,5)

escolha = int(input('Tente adivinhar qual número é o sorteado, dica: entre 0 e 5: '))
print(numero)
if escolha == numero:
    print('Você escolheu o número correto, parabéns :D')
else:
    print('Infelizmente você escolheu o número errado D:')