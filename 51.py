numero = int(input('Digite um número: '))
razão = int(input('Digite a razão: '))
décimotermo = numero + (10 -1) * razão
for c in range (numero, décimotermo + 1, razão):
    print(c)