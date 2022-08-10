numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
tabela = 0

while tabela != ('5'):
    tabela = str(input('''=-=-=-=-MENU=-=-=-=-
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    '''))
    if tabela == ('1'):
        print('A soma dos dois números que você digitou é: ', numero1 + numero2)
    elif tabela == ('2'):
        print('A multiplicação entre os números que você digitou é: ', numero1 * numero2)
    elif tabela == ('3'):
        if numero1 > numero2:
            print(numero1, 'é maior do que', numero2)
        elif numero2 > numero1:
            print(numero2, 'é maior do que', numero1)
    elif tabela == ('4'):
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
    if tabela == ('5'):
        print('Você saiu do programa!')
exit(0)