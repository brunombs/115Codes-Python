from time import sleep
def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {início} até {fim} com intervalos de {passo}')

    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += passo
            sleep(0.3)
        print('\n')
        print('FIM DA CONTAGEM\n')

    if início > fim:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo
            sleep(0.3)
        print('\n')
        print('FIM DA CONTAGEM\n')


contador(1, 10, 1)
contador(10, 0, 2)
primeiro = int(input('Digite o valor inicial: '))
segundo = int(input('Digite o valor final: '))
passo = int(input('Digite o intervalo entre os valores: '))
contador(primeiro, segundo, passo)