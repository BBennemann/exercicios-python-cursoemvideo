def area():
    print('Controle de Terrenos')
    print('-' * 25)
    n1 = float(input('LARGURA (m): '))
    n2 = float(input('COMPRIMENTO (m): '))
    print('A area de um terreno {}X{} é de {}m².'.format(n1, n2, n1 * n2))


while True:
    area()
    n3 = str(input('Quer continuar? ')).upper()[0]
    print('-' * 25)
    if n3 in 'Nn':
        break
print('Fim do programa')
