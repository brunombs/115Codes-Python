import math
numero = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(numero))
cos = math.cos(math.radians(numero))
tangente = math.tan(math.radians(numero))
print('O ângulo de {} tem o SENO de {:.2f}'.format(numero, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(numero, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(numero, tangente))
