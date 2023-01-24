import moeda107
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor {numero}:
+ 10% = {moeda107.aumentar(numero, 10)}
- 10% = {moeda107.diminuir(numero, 10)}
* 2 = {moeda107.dobro(numero)}
/ 2 = {moeda107.metade(numero)}
''')
