import datetime
dicionário = dict()
dicionário['nome'] =str(input('Digite o nome: '))
dicionário['idade'] = int(input('Digite o ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - dicionário["idade"]
dicionário['carteira de trabalho'] = int(input('Digite o número da carteira de trabalho (0 se não tiver): '))
dicionário['ano de contratação'] = int(input('Digite o ano em que foi contratado: '))
dicionário['salário'] = int(input('Digite o seu salário: '))
dicionário['aposentadoria'] = (ano - dicionário["idade"] + dicionário["ano de contratação"] + 35) - ano
print(f'Nome tem o valor: {dicionário["nome"]}')
print(f'Idade tem o valor: {ano - dicionário["idade"]}')
print(f'CTPS tem o valor: {dicionário["carteira de trabalho"]}')
print(f'Contratação tem o valor: {dicionário["ano de contratação"]}')
print(f'Salário tem o valor: {dicionário["salário"]}')
print(f'Aposentadoria tem o valor: {dicionário["aposentadoria"]}')
