from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números gerados foram: {n}')
print(f'O maior número é o {max(n)}')
print(f'O menor número é o {min(n)}')