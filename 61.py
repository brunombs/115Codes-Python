numero = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão do número: '))
contador = 0
while contador < 11:
    print('O {}º termo da P.A é: {}'.format(contador, numero))
    numero = numero + razão
    contador += 1
print('Fim :D')