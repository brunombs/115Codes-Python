lista = list()
maior = 0
menor = 0
for cont in range (0, 5):
    lista.append(int(input(f'Digite um número inteiro para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
for c, v in enumerate (lista):
    print(f'Na posição {c} está o valor {v}')
print(f'O menor valor da lista é {menor} e o maior é {maior}')