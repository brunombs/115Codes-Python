números = list()
pares = list()
ímpares = list()
for cont in range(0, 7):
    números.append(int(input('Digite um número: ')))
    if números[cont] % 2 == 0:
        pares.append(números[cont])
    if números[cont] % 2 == 1:
        ímpares.append(números[cont])
print(números)
print(f'Os valores pares da lista são: {sorted(pares)}')
print(f'Os valores ímpares da lista são: {sorted(ímpares)}')
