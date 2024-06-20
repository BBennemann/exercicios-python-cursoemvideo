jogador = {}
gol = []
g = 0
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
n = int(input('Quantas partidas ele jogou? '))
for x in range(0, n):
    n1 = int(input('Quantos gols na partida {}? '.format(x)))
    g = g + n1
    gol.append(n1)
jogador['gols'] = gol
jogador['total'] = g
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, i in jogador.items():
    print('O campo {} tem o valor {}'.format(k, i))
print('-=' * 30)
print('O jogador {} jogou {} partidas'.format(jogador['nome'], n))
for c in range(0, n):
    print('   -> Na partida {}, ele fez {} gols'.format(c, jogador['gols'][c]))
print('Foi um total de {} gols'.format(jogador['total']))
print('-=' * 30)
