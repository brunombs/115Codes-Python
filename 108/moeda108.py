def aumentar(preço=0, taxa=0):
    aumentado = preço + (preço * taxa / 100)
    return aumentado


def diminuir(preço=0, taxa=0, formatado=False):
    diminuido = preço - (preço * taxa / 100)
    return diminuido


def dobro(preço=0, formatado=False):
    dobro = preço * 2
    return dobro


def metade(preço=0, formatado=False):
    metade = preço / 2
    return metade


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço}'.replace('.', ',')
