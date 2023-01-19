aluno = list()
while True:
    dados = [str(input('Nome: ')), [float(input('Nota 1: ')), float(input('Nota 2: '))]]
    aluno.append(dados)
    quercontinuar = str(input('Quer continuar? [S/N]: ')).upper()
    if 'N' in quercontinuar:
        break
print('-' * 26)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for c in range(0, len(aluno)):
    print(f'{c:<4}{aluno[c][0]:<10}{(aluno[c][1][0]+aluno[c][1][1])/2:>8.1f}')
while True:
    print('-' * 35)
    númeroaluno = int(input('Mostrar notas de qual aluno?: '))
    if númeroaluno <= len(aluno) -1:
        print(f'\033[31mNotas de {aluno[númeroaluno][0]} são: {aluno[númeroaluno][1]}\033[m')
    desejacontinuar = str(input('Deseja ver a nota de outro aluno? [S/N]: ')).upper()
    if desejacontinuar == 'N':
        print('Obrigado por usar o nosso boletim')
        break
