n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = 0
while n3 != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    n3 = int(input('>>>>> Qual é a sua opção? '))
    if n3 == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2 ,n1 + n2))
        print('=-' * 18)
    elif n3 == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        print('=-' * 18)
    elif n3 == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
            print('=-' * 18)
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
            print('=-' * 18)
    elif n3 == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-' * 18)
    elif n3 == 5:
        print('Finalizando...')
        print('=-' * 18)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção invalida. Tente novamente')
        print('=-' * 18)




