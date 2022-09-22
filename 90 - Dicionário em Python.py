aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('='*30)
print(f'A média de {aluno["nome"]} é: {aluno["média"]}')
if aluno["média"] >= 7:
    print('Aluno \033[32maprovado\033[m')
if aluno["média"] < 5:
    print('Aluno \033[31mreprovado\033[m')
if 5 <= aluno["média"] < 7:
    print('Aluno em \033[33mrecuperação\033[m')
for cadavaloremaluno, valoresdodicionário in aluno.items():
    print(f'{cadavaloremaluno} é igual a: {valoresdodicionário}')