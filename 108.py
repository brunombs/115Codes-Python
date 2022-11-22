import moeda
numero = float(input('Digite o preço em R$: '))
print(f'''
O valor R${numero}:
+ 10% = R${moeda.aumentar(numero):.3f}
- 10% = R${moeda.diminuir(numero):.3f}
* 2 = R${moeda.dobro(numero):.3f}
/ 2 = R${moeda.metade(numero):.3f}
''')