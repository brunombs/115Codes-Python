galera = list()
pessoa = dict()
pessoasregistradas = 0
média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = (str(input('Digite o nome: ')))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        pessoa['sexo'] = str(input('OPÇÃO INVÁLIDA, digite apenas "M" ou "F": ')).upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    média += pessoa['idade']
    pessoasregistradas += 1
    galera.append(pessoa.copy())
    quercontinuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    if quercontinuar == 'N':
        break
print(f'Foram cadastradas {pessoasregistradas} pessoas!')
print(f'A média de idade do grupo é: {int(média/pessoasregistradas)}')
print('O nome das mulheres da lista são: ')
for pessoa in galera:
    if pessoa['sexo'] in 'F':
        print(f'{pessoa["nome"]}')
print(f'O nome das pessoas com idade acima da média são:')
for pessoa in galera:
    if pessoa['idade'] > média/pessoasregistradas:
        print(f'{pessoa["nome"]} com idade {pessoa["idade"]}')
