cont = 0
n1 = int(input('Digite um numero: '))
for x in range(1, n1 + 1):
    if n1 % x == 0:
        print('\033[0;32m{}\033[m'.format(x), end=' ')
        cont = cont + 1
    else:
        print('\033[0;31m{}\033[m'.format(x), end=' ')
print('O numero {} foi divisivel {} vezes'.format(n1, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO é primo')
