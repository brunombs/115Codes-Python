dezeroatévinte = ('zero', 'um', 'dois', 'três', 'quatro',
                  'cinco', 'seis', 'sete', 'oito', 'nove',
                  'dez', 'onze', 'doze', 'treze', 'quatorze',
                  'quinze', 'dezesseis', 'dezessete',
                  'dezoito', 'dezenove', 'vinte')
while True:
    jogarnovamente = ' '
    número = int(input('Digite um valor de 0 até 20: '))
    while número < 0 or número > 20:
        número = int(input('Número inválido, digite um valor de 0 até 20: '))
    if 0 <= número <= 20:
        print(f'Esse número por extenso se escreve: {dezeroatévinte[número]}')
    while jogarnovamente not in ('S', 'N'):
        jogarnovamente = str(input('Você quer jogar novamente? [S/N]: ')).upper()
    if jogarnovamente == 'N':
        break
print('Obrigado por participar!')