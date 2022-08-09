valordoproduto = float(input('Digite o preço do produto que deseja comprar: '))
condição = int(input('''
Escolha uma forma para pagamento:
[1] À VISTA (dinheiro ou cheque)
[2] CARTÃO à vista
[3] CARTÃO até 2x
[4] CARTÃO até 3x
'''))

if condição == 1:
    print('O produto à vista tem 10% de desconto e o valor atualizado é: {:.2f}'.format(valordoproduto * 0.9))
elif condição == 2:
    print('O produto no cartão à vista tem 5% de desconto e o valor atualizado é: {:.2}'.format(valordoproduto * 0.95))
elif condição == 3:
    print('O produto no cartão em até 2x tem o preço normal!')
elif condição == 4:
    print('O produto no cartão parcelado em 3x ou mais tem aumento de 20% do valor, totalizando: {:.2f}'.format(valordoproduto * 1.20))
else:
    print('Opção de pagamento inválida, tente novamente!')