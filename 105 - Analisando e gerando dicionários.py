def notas(num, situação=False):
    """
    Função para analisar a quantidade de notas, maior nota, menor nota, média e situação de alunos!
    :param num: as notas do aluno!
    :param situação: valor opcional para saber se o aluno está numa situação boa, razoável ou ruim!
    :return: dicionário com várias situações sobre a situação do aluno!
    """
    dici = {}
    dici["Quantidade de notas"] = len(num)
    dici["Maior nota"] = max(num)
    dici["Menor nota"] = min(num)
    dici["Média"] = sum(num) / len(num)
    if situação:
        if dici["Média"] >= 7:
            dici["Situação"] = 'SITUAÇÃO DO ALUNO É BOA!'
        if dici["Média"] >= 5 and dici["Média"] < 7:
            dici["Situação"] = 'SITUAÇÃO DO ALUNO É RAZOÁVEL!'
        if dici["Média"] < 5:
            dici["Situação"] = 'SITUAÇÃO DO ALUNO É RUIM!'
    return dici

nota = list()
while True:
    resp = float(input('Digite a nota que você quer adicionar: '))
    nota.append(resp)
    quercontinuar = str(input('Quer adicionar outra nota? [S/N]: ')).upper()
    if quercontinuar == 'N':
        break

resposta = (notas(nota, situação=True))
print(resposta)
help(notas)
