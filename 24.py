nomedacidade = str(input('Digite o nome de alguma cidade: ')).strip()

print('O nome da cidade começa com Santo?')
print(nomedacidade[:5].upper() == 'SANTO')