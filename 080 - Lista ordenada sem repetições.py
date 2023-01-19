números = list()
for contador in range (0, 5):
    número = int(input('Digite um número: '))
    if contador == 0 or número > números[-1]:
        números.append(número)
        print(f'O valor {número} foi adicionado ao final da lista... ')
    else:
        pos = 0
        while pos < len(números):
            if número <= números[pos]:
                números.insert(pos, número)
                print(f'{número} adicionado na posição {pos} da lista!')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {números}')
