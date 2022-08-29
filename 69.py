homem = 0
mulher = 0
pessoasdezoito = 0
mulheresmenosdevinte = 0
while True:
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        pessoasdezoito += 1
    sexo = str(input('Digite o seu sexo: [M/F]: ')).upper()
    while sexo not in ('M', 'F'):
        sexo = str(input('Opção inválida, tente novamente! Digite "M" para masculino e "F" para feminino: ')).upper()
    if sexo == ('M'):
        homem += 1
    elif sexo == ('F') and idade <= 20:
        mulheresmenosdevinte += 1
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    while continuar != ('S') and continuar != ('N'):
        continuar = str(input('Opção inválida, tente novamente! Digite "S" para sim e "N" para não: ')).upper()
    if continuar == ('N'):
        break
print(f'{pessoasdezoito} pessoa(s) tem dezoito anos ou mais.')
print(f'Foram cadastrados {homem} homem(s)!')
print(f'{mulheresmenosdevinte} mulher(es) tem menos de vinte anos.')