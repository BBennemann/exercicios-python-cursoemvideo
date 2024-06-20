n1 = int(input('Qual a velocidade do carro em Km: '))
n2 = (n1 - 80) * 7
if n1 <= 80:
    print('Voce esta no limite de velocidade, tenha uma boa viajem.')
else:
    print('''Voce esta acima do limite de velocidade, pague {} R$ de multa'''.format(n2))
