from random import randint
from time import sleep
numeros = []
def sorteia():
    cont = 0
    while cont < 5:
        numerosorteado = randint(0, 100)
        numeros.append(numerosorteado)
        cont += 1
        print(f'O {cont}º número sorteado foi: {numerosorteado}')
        sleep(0.3)
def somaPar():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'O valor total da soma dos números pares da lista é: {soma}')

sorteia()
somaPar()
