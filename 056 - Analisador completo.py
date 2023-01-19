soma = 0
maioridadehomem = 0
nomedomaisvelho = ''
menorde20 = 0
for c in range (1, 5):
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo M/F: ')).strip()
    soma = soma + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        menorde20 += 1
print('A média de idade do grupo é: {} anos'.format(soma/4))
print('O nome do homem mais velho é: {}.'.format(nomedomaisvelho))
print('{} mulheres tem menos de 20 anos'.format(menorde20))
