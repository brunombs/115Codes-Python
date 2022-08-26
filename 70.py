quercontinuar = str(input('Você quer jogar? [S/N]: ')).upper()
while quercontinuar != ('S') and quercontinuar != ('N'):
    quercontinuar = str(input('Opção inválida, tente novamente! Digite "S" para SIM e "N" para não: ')).upper()
    if quercontinuar == ('N'):
        break
totalgasto = 0
maiorquemil = 0
maisbarato = 0
últimopreço = 0
preçobarato = 0
while quercontinuar == ('S'):
    nomedoproduto = str(input('Digite o nome do produto: '))
    preçodoproduto = float(input('Digite o valor do produto: '))
    totalgasto += preçodoproduto
    if preçodoproduto >= 1000:
        maiorquemil += 1
    elif preçodoproduto <= últimopreço:
        maisbarato = nomedoproduto
        preçobarato = preçodoproduto
    últimopreço = preçodoproduto
    quercontinuar = str(input('Você quer continuar? [S/N]: ')).upper()
    while quercontinuar != ('S') and quercontinuar != ('N'):
        quercontinuar = str(input('Opção inválida, tente novamente! Digite "S" para SIM e "N" para não: ')).upper()
        if quercontinuar == ('N'):
            break
print(f'O valor total gasto foi {totalgasto} R$')
print(f'{maiorquemil} produto(s) custa(m) mais de 1.000 R$')
print(f'{maisbarato} é o produto mais barato e custou R$ {preçobarato}')