times =('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('Lista de times do Brasileirao: {}'.format(times))
print('-=' * 60)
print('Os 5 primeiros sao {}'.format(times[:5]))
print('-=' * 60)
print('OS 4 ultimos sao {}'.format(times[-4:]))
print('-=' * 60)
print('Times em ordem alfabetica {}'.format(sorted(times)))
print('-=' * 60)
print('O chapecoense esta na {}ª posiçao'.format(times.index('Chapecoense')+1))


