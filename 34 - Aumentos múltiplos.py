salario = int(input('Digite o seu salário: '))
if salario > 1250:
    print('Seu novo salário é: R${}'.format(salario*1.10))
else:
    print('Seu novo salário é: R${}'.format(salario*1.15))
