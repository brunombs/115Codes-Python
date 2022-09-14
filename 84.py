nomeepeso = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(nomeepeso) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    nomeepeso.append(dado[:])
    dado.clear()
    quercontinuar = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).upper()
    while quercontinuar != 'S' and quercontinuar != 'N':
        print('Opção inválida, digite apenas "S" ou "N"')
        quercontinuar = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).upper()
    if quercontinuar == 'N':
        break
print('-'*60)
print(f'Os dados cadastrados foram: {nomeepeso}')
print(f'A quantidade de pessoas cadastradas foi: {len(nomeepeso)}')
print(f'O maior peso foi de {maior} kg, peso de: ', end='')
for contador, nome in enumerate(nomeepeso):
    if maior == nome[1]:
        print(f'{nome[0]}...', end='')
print()
print(f'O menor peso foi de {menor} kg, peso de: ', end='')
for contador, nome in enumerate(nomeepeso):
    if menor == nome[1]:
        print(f'{nome[0]}...', end='')
print()
print('-'*60)