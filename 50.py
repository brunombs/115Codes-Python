p = 0
i = 0
for c in range (0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        p = p + numero
    elif numero % 2 == 1:
        i = i + numero
print('A soma dos valores pares é {}'.format(p))
print('A soma dos valores ímpares é {}'.format(i))
print('Fim')