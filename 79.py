números = list()
while True:
    número = int(input('Digite um número para ser adicionado a uma lista: '))
    if número not in números:
        números.append(número)
        print('Número adicionado com sucesso!')
    else:
        print('Número não adicionado pois já estava na lista!')
    quercontinuar = str(input('Você quer adicionar outro número? [S/N]: ')).upper()
    while quercontinuar != "S" and quercontinuar != "N":
        quercontinuar = str(input('Opção inválida, digite apenas "S" ou "N": ')).upper()
    if quercontinuar != 'S':
        break
print(sorted(números))