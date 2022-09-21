números = [[], []]
for cont in range(1, 8):
    número = int(input(f'Digite o {cont}ª número inteiro: '))
    if número % 2 == 0:
        números[1].append(número)
    if número % 2 == 1:
        números[0].append(número)
print(f'A lista com todos os números digitados é: \033[31m{números}\033[m')
print(f'A lista em ordem crescente dos números pares é: \033[32m{sorted(números[1])}\033[m')
print(f'A lista em ordem crescente dos números ímpares é: \033[33m{sorted(números[0])}\033[m')
