def contador(i, f, p):
    print('Contagem de {} até {} de {} em {}'.format(i, f, p, p))

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('FIM!')
        print('-=' * 20)
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('FIM!')
        print('-=' * 20)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem.')
n1 = int(input('INICIO: '))
n2 = int(input('FIM: '))
n3 = int(input('PASSO: '))
contador(n1, n2, n3)
