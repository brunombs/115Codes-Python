import random
jokenpo = int(input('''
Escolha uma opção:
[1] Pedra
[2] Papel
[3] Tesoura
'''))
pedra = ('pedra')
papel = ('papel')
tesoura = ('tesoura')
lista = [pedra, papel,  tesoura]
computador = random.choice(lista)
if jokenpo == 1 and computador == pedra:
    print('Empate, o computador também escolheu {}.'.format(computador))
elif jokenpo == 1 and computador == papel:
    print('Você perdeu, o computador escolheu {}.'.format(computador))
elif jokenpo == 1 and computador == tesoura:
    print('Você ganhou, o computador escolheu {}.'.format(computador))
elif jokenpo == 2 and computador == pedra:
    print('Você ganhou, o computador escolheu {}.'.format(computador))
elif jokenpo == 2 and computador == papel:
    print('Empate, o computador escolheu {}.'.format(computador))
elif jokenpo == 2 and computador == tesoura:
    print('Você perdeu,o computador escolheu {}.'.format(computador))
elif jokenpo == 3 and computador == pedra:
    print('Você perdeu,o computador escolheu {}.'.format(computador))
elif jokenpo == 3 and computador == papel:
    print('Você ganhou, o computador escolheu {}.'.format(computador))
elif jokenpo == 3 and computador == tesoura:
    print('Empate, o computador escolheu {}.'.format(computador))