from random import randint
from time import sleep
lista = list()
jogos = list()
quantasvezes = int(input('Quantos jogos deseja sortear?: '))
total = 1
while total <= quantasvezes:
    cont = 0
    while True:
        número = randint(1, 60)
        if número not in lista:
            lista.append(número)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for cadajogo, resultadodojogo in enumerate(jogos):
    print(f'O jogo {cadajogo+1} é: {jogos[cadajogo]}')
    sleep(0.5)
print('BOA SORTE')
