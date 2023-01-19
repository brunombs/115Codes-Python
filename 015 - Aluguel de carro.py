km = float(input('Digite a quantidade de KMs que percorreu: '))
dias = float(input('Digite a quantidade de dias que permaneceu com o carro: '))
preco = (km*0.15) + (dias*60)
print('O preço a ser pago pelo aluguel do carro é {:.2f} reais. '.format(preco))
