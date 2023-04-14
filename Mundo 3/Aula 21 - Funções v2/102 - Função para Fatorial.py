def fatorial(num, show=False):
    f = 1
    for cont in range(num, 0, -1):
        if show == True:
            print(cont, end='')
            if cont > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= cont
    return f


calculocompleto = input('Você deseja ver o cálculo completo? Digite "S" ou "N": ').upper()
while 'S' not in calculocompleto and 'N' not in calculocompleto:
    calculocompleto = input('OPÇÃO INVÁLIDA! Digite apenas "S" ou "N": ').upper()
if calculocompleto == 'N':
    calculocompleto = False
if calculocompleto == 'S':
    calculocompleto = True
valor = int(input('Digite o número que você gostaria de saber o fatorial: '))
print(fatorial(valor, show=calculocompleto))
