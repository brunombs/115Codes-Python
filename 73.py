tabela = ('palmeiras', 'flamengo', 'fluminense', 'corinthians', 'athletico-pr',
          'internacional', 'atlético-mg', 'santos', 'américa-mg', 'goiás',
          'bragantino', 'fortaleza', 'são paulo', 'botafogo', 'ceará sc',
          'coritiba', 'cuiabá', 'avaí', 'atlético-go', 'juventude')

print('-=' * 15)
print(tabela)
print('-=' * 15)
print(f'Os cinco primeiros colocados do Campeonato Brasileiro na série A em 2022 no dia 29/08/2022'
      f' são, respectivamente: {tabela[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados do Campeonato Brasileiro na série A em 2022 no dia 29/08/2022'
      f' são: {tabela[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print('-=' * 15)
print(f'O Corinthians está na {tabela.index("corinthians")} posição')
print('-=' * 15)