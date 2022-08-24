from random import randint
parouimpar = str(input('Você quer jogar de par ou ímpar? ')).upper()
while parouimpar != ('IMPAR') and parouimpar != ('PAR'):
    parouimpar = str(input('Opção inválida, digite apenas "PAR" ou "IMPAR": ')).upper()
numeroescolhido = int(input('Qual número você quer jogar? '))
computador = randint(1, 10)
c = -1
valor = numeroescolhido + computador
while parouimpar == ('PAR'):
    c += 1
    if parouimpar == ('PAR') and valor % 2 == 0:
        print(f'Você venceu pois escolheu par e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é par!')
        numeroescolhido = int(input('Jogue novamente, escolha outro número: '))
        computador = randint(1, 10)
        valor = numeroescolhido + computador
    else:
            print(f'Você perdeu para o computador pois ele jogou {computador} e você {numeroescolhido} resultando em: {valor}, que é número ímpar')
            break
while parouimpar == ('IMPAR'):
    c += 1
    if parouimpar == ('IMPAR') and valor % 2 != 0:
        print(f'Você venceu pois escolheu impar e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é impar!')
        numeroescolhido = int(input('Jogue novamente, escolha outro número: '))
        computador = randint(1, 10)
        valor = numeroescolhido + computador
    else:
        print(f'Você perdeu pois escolheu ímpar e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é par!')
        break
print(f'Você venceu {c} vez(es) seguida(s)')
