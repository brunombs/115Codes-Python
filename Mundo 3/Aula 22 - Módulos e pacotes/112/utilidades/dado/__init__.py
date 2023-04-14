def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            valid = True
            return float(entrada)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
    else:
         print('ERRO! Digite um NÚMERO INTEIRO:')
         if ok:
             break
    return valor