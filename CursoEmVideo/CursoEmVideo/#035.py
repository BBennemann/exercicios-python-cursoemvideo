n1 = int(input('Informe o lado do triangulo: '))
n2 = int(input('Informe o segundo lado do triangulo: '))
n3 = int(input('Informe o terceiro lado do triangulo: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('O triangulo {} {} {} existe'.format(n1, n2, n3))
else:
    print('O triangulo {} {} {} n existe'.format(n1, n2, n3))



