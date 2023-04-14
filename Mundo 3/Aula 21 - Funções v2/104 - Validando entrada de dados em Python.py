def leiaInt(numero):
    if numero.isnumeric():
        print(f'Você acabou de digitar o número {numero}')
    else:
        while True:
            numero = str(input('ERRO! Digite um NÚMERO INTEIRO:'))
            if numero.isnumeric():
                print(f'Você acabou de digitar o número {numero}')
                break


numero = str(input('Digite um número: '))
leiaInt(numero)
