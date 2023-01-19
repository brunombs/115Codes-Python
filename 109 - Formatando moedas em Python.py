import moeda
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor {numero}:
+ 10% = {moeda.aumentar(numero, 20)}
- 10% = {moeda.diminuir(numero, 10)}
* 2 = {moeda.dobro(numero, True)}
/ 2 = {moeda.metade(numero)}
''')
