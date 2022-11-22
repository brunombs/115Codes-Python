from random import randint
c = ('\033[m',              #0 -sem cor
     '\033[0;30;41m',       #1 - vermelho
     '\033[0;30;42m',       #2 - verde
     '\033[0;30;43m',       #3 - amarelo
     '\033[0;30;44m',       #4 - azul
     '\033[0;30;45m',       #5 - roxo
     '\033[7;30m',       #6 - branco
)

def ajuda(com):
    print(c[corsorteada], end='')
    help(com)
    print(c[corsorteada], end='')


def título(msg, cor=0):
    print(c[cor], end='')
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print(c[0], end='')


comando = ''
while True:
    corsorteada = randint(0, 6)
    título('SISTEMA DE AJUDA PyHELP', corsorteada)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ A PRÓXIMA!', corsorteada)