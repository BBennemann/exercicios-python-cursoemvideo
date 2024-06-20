n1 = int(input('Qual a distancia da viagem em Km? '))
if n1 <= 200:
    print('o valor da viagem sera de {} R$'.format(n1 * 0.5))
else:
    print('o valor da viagem sera de {} R$'.format(n1 * 0.45))

