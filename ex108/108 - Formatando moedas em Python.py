import moeda108
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor {moeda108.moeda(numero)}:
+ 10% = {moeda108.moeda(moeda108.aumentar(numero, 10))}
- 10% = {moeda108.moeda(moeda108.diminuir(numero, 10))}
* 2 = {moeda108.moeda(moeda108.dobro(numero))}
/ 2 = {moeda108.moeda(moeda108.metade(numero))}
''')
