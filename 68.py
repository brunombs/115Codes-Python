from random import randint
c = 0
while True:
    parouimpar = ' '
    computador = randint(1, 10)
    while parouimpar not in ('IMPAR', 'PAR'):
        parouimpar = str(input('Você quer jogar de par ou ímpar? ')).upper()
        while parouimpar not in ('IMPAR', 'PAR'):
            parouimpar = str(input('Opção inválida, digite apenas "PAR" ou "IMPAR": ')).upper()
    numeroescolhido = int(input('Qual número você quer jogar? '))
    valor = numeroescolhido + computador
    if parouimpar == ('PAR'):
        if parouimpar == ('PAR') and valor % 2 == 0:
            print(f'Você venceu pois escolheu par e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é par!')
            c += 1
        else:
            print(f'Você perdeu para o computador pois ele jogou {computador} e você {numeroescolhido} resultando em: {valor}, que é número ímpar')
            break
    if parouimpar == ('IMPAR'):
        if parouimpar == ('IMPAR') and valor % 2 != 0:
            print(f'Você venceu pois escolheu impar e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é impar!')
            c += 1
        else:
            print(f'Você perdeu pois escolheu ímpar e jogou {numeroescolhido} e o computador jogou {computador} resultando no valor {valor} que é par!')
            break
print(f'Você venceu {c} vez(es) seguida(s)')