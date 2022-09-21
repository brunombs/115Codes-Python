lista = list()
menor = 0
maior = 0
for contador in range (0, 5):
    lista.append(int(input(f'Digite um número nas posições {contador}: ')))
    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]
print('='*60)
print(f'Você digitou os valores: {lista}')
print('='*60)
print(f'O maior número digitado foi: {maior} nas posições: ', end='')
for contador, número in enumerate(lista):
    if maior == número:
        print(f'{contador}... ', end='')
print()
print(f'O menor número digitado foi: {menor} nas posições: ', end='')
for contador, número in enumerate(lista):
    if menor == número:
        print(f'{contador}... ', end='')
print()
print('='*60)
