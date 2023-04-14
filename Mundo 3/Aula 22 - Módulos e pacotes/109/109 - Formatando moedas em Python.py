import moeda109
numero = float(input('Digite o preço em R$: '))
print(f'''
O preço R${numero}:
+ 20% = {moeda109.aumentar(numero, 20, True)}
- 10% = {moeda109.diminuir(numero, 10, True)}
* 2 = {moeda109.dobro(numero, True)}
/ 2 = {moeda109.metade(numero, True)}
''')
