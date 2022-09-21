sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
while sexo != ('M') and sexo != ('F'):
    print('Opção inválida, digite apenas "M" ou "F", sem as aspas!')
    sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
if sexo == ('M'):
    sexo = ('masculino')
elif sexo == ('F'):
    sexo = ('feminino')
print('Você é do sexo {}!'.format(sexo))
