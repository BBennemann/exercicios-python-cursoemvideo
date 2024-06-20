def maior(*num):
    cont = maio = 0
    print('-=' * 20)
    print('analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        if cont == 0:
            maio = v
        elif v > maio:
            maio = v
        cont += 1
    print('Foram informados {} valores ao todo'.format(cont))
    print('O maior valor é {}'.format(maio))


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
