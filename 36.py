valordacasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
quantosanos = float(input('Digite com quantos anos irá pagar: '))
salariopermitido = salario * 0.3
prestacao = valordacasa / (quantosanos * 12)
print('30% do seu salário é equivalente a: {}.'.format(salariopermitido))

if prestacao > salariopermitido:
    print('Infelizmente o empréstimo foi negado pois excedeu 30% do salário mensal')
else:
    print('Parabéns, o seu empréstimo foi aprovado!')
    print('Você terminará de pagar o empréstimo da casa em {} anos pagando parcelas de R$ {}.'.format(quantosanos,
                                                                                                      prestacao))