s1= float(input('Primeira reta: '))
s2= float(input('Segunda reta: '))
s3= float(input('Terceira reta: '))
triangulo = s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2

if triangulo and s1 == s2 == s3:
    print('Esse é um triângulo equilátero, isso porque tem todos os lados iguais')
elif triangulo and s1 == s2 != s3 or s2 == s3 != s1 or s1 == s3 != s2:
    print('Esse é um triângulo isósceles, isso porque tem dois lados iguais')
elif triangulo and s1 != s2 != s3:
    print('Esse é um triângulo escaleno, isso porque tem os três lados distintos')
else:
    print('As retas escolhidas não formam um triângulo')