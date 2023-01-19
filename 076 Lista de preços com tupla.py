nomeevalor = ('iPad', 100, 'Apple Watch', 500, 'iPhone', 1200, 'MacBook', 1500)
print('-'*40)
print('LISTA COM NOME DOS PRODUTOS E PREÇOS')
print('-'*40)
for pos in range(0, len(nomeevalor)):
    if pos % 2 == 0:
        print(f'{nomeevalor[pos]:.<30}R$', end='')
    else:
        print(f'{nomeevalor[pos]:>5}')
