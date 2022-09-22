from random import randint
from time import sleep
from operator import itemgetter
resultados = {'Jogador 1': randint(1, 6),
              'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}
ranking = dict()
for jogador, resultado in resultados.items():
    print(f'{jogador} foi sorteado com o número: {resultados[jogador]}')
    sleep(0.5)
print('='*50)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES')
for jogador, resultado in enumerate(ranking):
    print(f'{jogador+1}º lugar: {resultado[0]} com {resultado[1]}')
    sleep(0.5)