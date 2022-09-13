números = list()
while True:
    números.append(int(input('Digite um número: ')))
    quercontinuar = str(input('Quer continuar? [S/N]: ')).upper()
    if quercontinuar != 'S':
        break
print('-'* 60)
print(f'Você digitou {len(números)} números')
print('-'* 60)
números.sort(reverse=True)
print(f'Os números em ordem decrescente são: {números}')
print('-'* 60)
if 5 in números:
    estáounão = 'está'
else:
    estáounão = 'não está'
print(f'O valor 5 {estáounão} na lista.')
print('-'* 60)