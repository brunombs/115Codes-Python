n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('O primeiro número é: {}'.format(n1))
print('O segundo número é: {}'.format(n2))
print('O terceiro número é: {}'.format(n3))
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
if n2 > n1 and n2> n3:
    print('O maior número é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é {}'.format(n3))
