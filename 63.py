termos = int(input('Digite a quantidade de termos da sequência de fibonacci que você quer ver: '))
termo1 = 0
termo2 = 1
numero = 1

while numero <= termos:
    print('{}'.format(termo1), end='')
    total = termo1 + termo2
    termo1 = termo2
    termo2 = total
    print(' -> ' if numero < termos else ' -> FIM', end='')
    numero += 1