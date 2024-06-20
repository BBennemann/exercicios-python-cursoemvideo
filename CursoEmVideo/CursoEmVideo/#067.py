#cont = 1
#n1 = int(input('Quer ver a tabuada de qual valor: '))
#print('-' * 30)
#while True:
#    if n1 < 0:
#        break
#    print('{} x {} = {}'.format(n1, cont, n1 * cont))
#    cont = cont + 1
#    if cont == 11:
#        cont = 1
#        print('-' * 30)
#        n1 = int(input('Quer ver a tabuada de qual valor: '))
#        print('-' * 30)
#    if n1 < 0:
#        break
#print('Programa tabuada encerrado, volte sempre!')

while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n * c))
    print('-' * 30)
print('Programa tabuada encerrado, volte sempre!')