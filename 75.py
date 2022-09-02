valores = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: '))
print(valores)
print(f'O 9 aparece {valores.count(9)} vez(es)')
if 3 in valores:
    print(f'O primeiro valor 3 apareceu na posição {valores.index(3)}')
else:
    print('O valor 3 não foi digtado nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')