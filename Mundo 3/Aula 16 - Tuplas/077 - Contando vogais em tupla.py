palavras = ('apple', 'microsoft', 'windows', 'macos', 'python', 'front-end', 'back-end', 'fullstack', 'dev', 'linux')
print('VOGAIS')
for cont in palavras:
    print(f'\nNa palavra {cont.upper()}, temos a(s) vogal(is): ', end='')
    for vogais in cont:
        if vogais in 'aáãâeéêiíõôouúû':
            print(vogais, end=' ')
