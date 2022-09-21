tabuada = int(input('Digite o número que deseja saber a tabuada: '))
c = 1
while tabuada >= 0:
    while c < 10:
        c += 1
        print(f'{tabuada} * {c}: {tabuada * c}')
    c = 1
    tabuada = int(input('Digite o número que deseja saber a tabuada: '))
    if tabuada <= -1:
        break
print('Obrigado por participar')
