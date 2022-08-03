numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('A unidade desse número é {}'.format(unidade))
print('A dezena desse número é {}'.format(dezena))
print('A centena desse número é {}'.format(centena))
print('O milhar desse número é {}'.format(milhar))