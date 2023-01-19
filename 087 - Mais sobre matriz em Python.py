matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somaterceiracoluna = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        somaterceiracoluna += matriz[linha][2]
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^10}]', end='')
    print()
print('*-'*30)
print(f'A soma de todos os valores PARES é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somaterceiracoluna}')
print(f'O maior valor da segunda linha é: {maior}')
