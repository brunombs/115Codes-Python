print('CONTROLE DE TERRENOS')
print('-'*20)
def area(a, b):
    terreno = int(a * b)
    print(f'A área de um terreno {a} x {b} é de {terreno}m²')

largura = input('LARGURA (m): ')
largura = float(largura)
comprimento = input('COMPRIMENTO (m): ')
comprimento = float(comprimento)
print('-'*20)

area(largura, comprimento)
