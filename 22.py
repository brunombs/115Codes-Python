nome = str(input('Digite o seu nome completo: ')).strip()

print ('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu noime com todas as letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))