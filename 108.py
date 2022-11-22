import moeda
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor {moeda.moeda(numero)}:
+ 10% = {moeda.moeda(moeda.aumentar(numero, 10))}
- 10% = {moeda.moeda(moeda.diminuir(numero, 10))}
* 2 = {moeda.moeda(moeda.dobro(numero))}
/ 2 = {moeda.moeda(moeda.metade(numero))}
''')