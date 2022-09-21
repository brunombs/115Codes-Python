lista = list()
listapares = list()
listaimpares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    quercontinuar = str(input('Deseja adicionar outro número? [S/N]: ')).upper()
    if quercontinuar != 'S':
        break
print('-'* 60)
print(f'A lista com todos os números é: {lista}')
for contador, número in enumerate(lista):
    if número % 2 == 0:
        listapares.append(número)
    elif número % 1 == 0:
        listaimpares.append(número)
print(f'A lista com os números pares é: {listapares}')
print(f'A lista com os números impares é: {listaimpares}')
