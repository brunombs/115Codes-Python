nome = str(input('Digite o seu nome: ')).strip()
div = nome.upper().split()
print('Tem SILVA no seu nome? {}'.format('SILVA' in div))
