n1 = int(input('Informe o lado do triangulo: '))
n2 = int(input('Informe o segundo lado do triangulo: '))
n3 = int(input('Informe o terceiro lado do triangulo: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('O triangulo {} {} {} existe'.format(n1, n2, n3))
    if n1 == n2 and n1 == n3:
        print('O triangulo é equilatero')
    elif n1 == n2 or n1 == n3 or n3 == n2:
        print('O triangulo é isoceles')
    else:
        print('O triangulo é escaleno')
else:
    print('O triangulo {} {} {} n existe'.format(n1, n2, n3))



