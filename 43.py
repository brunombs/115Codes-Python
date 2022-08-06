peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em M: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print('Você está abaixo do peso.')
if imc > 18.5 and imc <= 25:
    print('Você está no peso ideal')
if imc > 25 and imc <= 30:
    print('Você está com sobrepeso')
if imc > 30 and imc <= 40:
    print('Você está com obesidade')
if imc > 40:
    print('Você está com obesidade mórbida')
print('Seu IMC é: {:.4}'.format(imc))