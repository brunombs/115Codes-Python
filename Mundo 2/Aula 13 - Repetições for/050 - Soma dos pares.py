p = 0
i = 0
np = 0
ni = 0
for c in range (0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        p = p + numero
        np += 1
    elif numero % 2 == 1:
        i = i + numero
        ni += 1
print('Você informou {} números pares e a soma desses valores é {}'.format(np, p))
print('Você informou {} números ímpares e a soma desses valores é {}'.format(ni, i))
print('Fim')
