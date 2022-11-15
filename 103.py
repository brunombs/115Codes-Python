def ficha(nome='desconhecido', goals=0):
    print(f'O jogador {nome} fez {goals} gol(s)!')

nomedojogador = str(input('Digite o nome do jogador: '))
gols = str(input(f'Digite quantos gols {nomedojogador}fez: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nomedojogador.strip() == '':
    ficha(goals = gols)
else:
    ficha(nomedojogador, gols)