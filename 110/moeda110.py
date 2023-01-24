def aumentar(preço=0, taxa=0, formatado=False):
    aumentado = preço + (preço * taxa / 100)
    return aumentado if formatado is False else moeda(aumentado)


def diminuir(preço=0, taxa=0, formatado=False):
    diminuido = preço - (preço * taxa / 100)
    return diminuido if formatado is False else moeda(diminuido)


def dobro(preço=0, formatado=False):
    dobro = preço * 2
    return dobro if formatado is False else moeda(dobro)


def metade(preço=0, formatado=False):
    metade = preço / 2
    return metade if formatado is False else moeda(metade)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metade do preço: \t{moeda(metade(preço))}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)