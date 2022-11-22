def aumentar(preço=0, taxa=0, formatado=False):
    aumentado = preço + (preço * taxa / 100)
    return aumentado if format is False else moeda(aumentado)


def diminuir(preço=0, taxa=0, formatado=False):
    diminuido = preço - (preço * taxa / 100)
    return diminuido if format is False else moeda(diminuido)


def dobro(preço=0, formatado=False):
    dobro = preço * 2
    return dobro if format is False else moeda(dobro)


def metade(preço=0, formatado=False):
    metade = preço / 2
    return metade if format is False else moeda(metade)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
