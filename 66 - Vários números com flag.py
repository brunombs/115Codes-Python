numero = soma = contador = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A soma dos valores é {soma}')
print(f'Foram digitados {contador} números')
