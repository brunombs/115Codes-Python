primeirotermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('O {}º termo da P.A é {}.'.format(contador, primeirotermo))
        primeirotermo += razão
        contador += 1
    print('˜continuação˜')
    mais = int(input('Digite quantos termos você ainda quer ver: '))
