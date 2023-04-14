s = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        print(c)
        s = s + c
print('Fim')
print('A soma de todos os valores é:', s)
