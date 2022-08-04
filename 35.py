s1= float(input('Primeira reta: '))
s2= float(input('Segunda reta: '))
s3= float(input('Terceira reta: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('As retas escolhidas formam um triângulo')
else:
    print('As retas escolhidas não formam um triângulo')