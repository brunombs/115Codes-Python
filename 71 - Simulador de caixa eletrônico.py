print('=-='*12)
print('Digite o valor que deseja sacar: ')
print('=-='*12)
valorasacar = int(input())
notasde50 = (valorasacar // 50)
restode50 = valorasacar % 50
notasde20 = (restode50 // 20)
restode20 = restode50 % 20
notasde10 = (restode20 // 10)
restode10 = restode20 % 10
notasde1 = (restode10 // 1)
cédulas = notasde50 + notasde20 + notasde10 + notasde1
print(f'A máquina irá te entregar {cédulas} cédulas')
print(f'notas de 50: {notasde50}')
print(f'notas de 20: {notasde20}')
print(f'notas de 10: {notasde10}')
print(f'notas de 1: {notasde1}')
