dados = dict()
dados['nomedojogador'] = str(input('Digite o nome do jogador: '))
dados['quantaspartidas'] = int(input(f'Digite quantas partidas {dados["nomedojogador"]} jogou: '))
dados['totaldegols'] = 0
gols = list()
for partida in range(1, dados["quantaspartidas"]+1):
    quantosgols = int(input(f'Quantos gols {dados["nomedojogador"]} fez na partida {partida}: '))
    gols.append(quantosgols)
    dados["totaldegols"] += quantosgols
print('='*30)
print(dados)
print(f'Nome do jogador: {dados["nomedojogador"]}')
print(f'Gols feitos: {gols}')
print(f'O total de gols é: {dados["totaldegols"]}')
print('='*30)
print(f'O jogador {dados["nomedojogador"]} jogou {dados["quantaspartidas"]} partidas!')
for partida in range(0, dados["quantaspartidas"]):
    print(f'Na partida {partida+1}, fez {gols[partida]} gols')
