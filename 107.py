import moeda
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor {numero}:
+ 10% = {moeda.aumentar(numero, 10):.3f}
- 10% = {moeda.diminuir(numero, 10):.3f}
* 2 = {moeda.dobro(numero):.3f}
/ 2 = {moeda.metade(numero):.3f}
''')