velocidade = int(input('Digite a média da velocidade que você acha que os veículos na sua cidade trafegam: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Acima de 80km/h já é multado nas principais vias')
    print('Na velocidade que você informou, o condutor é multado em {} reais'.format(multa))
else:
    print('Até essa velocidade não tem multa :D')
