nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média foi {}'.format(media))
if media < 5:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')