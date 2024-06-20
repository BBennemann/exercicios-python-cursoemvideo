def ficha(n='<desconhecido>', g=0):
    return 'O jogador {} fez {} gol(s) no campeonato.'.format(n, g)


print('-' * 20)
n1 = str(input('Nome do jogador: '))
n2 = str(input('Numero de gols: '))
if n2.isnumeric():
    n2 = int(n2)
else:
    n2 = 0
if n1.strip() == '':
    print(ficha(g=n2))
else:
    print(ficha(n1, n2))
