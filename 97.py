def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))

while True:
    frase = input('Escreva algo: ')
    escreva(frase)
    quercontinuar = input('Quer continuar? digite "S" ou "N": ').upper()
    if quercontinuar == 'N':
        break
print('Obrigado por participar :D')