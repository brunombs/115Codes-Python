maiorpeso = 0
menorpeso = 0
for peso in range (1, 6):
    pesodapessoa = float(input('Digite o peso da {}ª pessoa: '.format(peso)))
    pesoatual = pesodapessoa
    if peso == 1:
        maiorpeso = pesodapessoa
        menorpeso = pesodapessoa
    else:
        if pesodapessoa > maiorpeso:
            maiorpeso = pesodapessoa
        if pesodapessoa < menorpeso:
            menorpeso = pesodapessoa
print('A pessoa com menor peso tem: {}kg'.format(menorpeso))
print('A pessoa com maior peso tem: {}kg'.format(maiorpeso))
