import statistics


def maior(* valores):
    for numero in valores:
        print(numero, end=' ')
    print(f'- Foram informados {len(valores)} valores')
    print(f'O maior valor informado foi {max(valores)}')
    print(f'O menor valor informado foi {min(valores)}')
    print(f'O valor médio informado foi {statistics.mean(valores)}')

maior(1, 3, 5, 7, 10, 33)