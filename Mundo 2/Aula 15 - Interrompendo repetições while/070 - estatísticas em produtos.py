totalgasto = maiorquemil = nomedomaisbarato = preçodomaisbarato = últimopreço = c = 0
quercontinuar = ' '
while True:
    nomedoproduto = str(input('Digite o nome do produto: '))
    preçodoproduto = float(input('Digite o valor do produto: '))
    c += 1
    if nomedomaisbarato == 0:
        maisbarato = nomedoproduto
    if c == 1:
        preçodomaisbarato = preçodoproduto
        nomedomaisbarato = nomedoproduto
    else:
        if preçodoproduto < preçodomaisbarato:
                preçodomaisbarato = preçodoproduto
                nomedomaisbarato = nomedoproduto
    totalgasto += preçodoproduto
    if preçodoproduto >= 1000:
        maiorquemil += 1
    quercontinuar = str(input('Você quer continuar? [S/N]: ')).upper()
    while quercontinuar != ('S') and quercontinuar != ('N'):
        quercontinuar = str(input('Opção inválida, tente novamente! Digite "S" para SIM e "N" para não: ')).upper()
    if quercontinuar == ('N'):
        break
print(f'O valor total gasto foi {totalgasto} R$')
print(f'{maiorquemil} produto(s) custa(m) mais de 1.000 R$')
print(f'{nomedomaisbarato} é o produto mais barato e custou R$ {preçodomaisbarato}')
