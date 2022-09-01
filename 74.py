from random import random
n1 = random()
n2 = random()
n3 = random()
n4 = random()
n5 = random()
listagem = (n1, n2, n3, n4, n5)
print(listagem)
if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    print(f'{n1} é o menor número')
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    print(f'{n2} é o menor número')
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    print(f'{n3} é o menor número')
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    print(f'{n4} é o menor número')
elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    print(f'{n5} é o menor número')
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f'{n1} é o maior número')
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(f'{n2} é o maior número')
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print(f'{n3} é o maior número')
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print(f'{n4} é o maior número')
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print(f'{n5} é o maior número')
