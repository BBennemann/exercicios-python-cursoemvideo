from random import randint
from operator import itemgetter # IMPORTANTE
dados = {}
ranking = []
print('Valores sorteados: ')
for x in range(1, 5):
    dados['jogador {}'.format(x)] = randint(1, 6)
for k, i in dados.items():
    print('{} tirou {} no dado'.format(k, i))
print('-=' * 20)
print('Ranking dos jogadores')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) # IMPORTANTE
for k, i in enumerate(ranking):
    print('{}° lugar: {} com {}'.format(k + 1, i[0], i[1]))

