jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        quercontinuar = str(input('Quer continuar? [S/N]: ')).upper()
        if quercontinuar in 'SN':
            break
        print('ERRO! Responda apenas "S" ou "N".')
    if quercontinuar == 'N':
        break
print('*'*30)
print('cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for indice, jogador in enumerate(time):
    print(f'{indice:>3} ', end='')
    for d in jogador.values():
        print(f'{str(d):15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'   No jogo {indice+1}, fez {gols} gols!')
    print('-' * 40)
print('Obrigado por participar!')