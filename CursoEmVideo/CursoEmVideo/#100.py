from random import randint
num = []


def sorte():
    for x in range(0, 5):
        n1 = randint(0, 10)
        num.append(n1)
    print('Sorteando 5 valores na lista: ', end='')
    for x in num:
        print(x, end=' ')
    print('PRONTO!')


def soma():
    n3 = 0
    for x, c in enumerate(num):
        n2 = c % 2
        if n2 == 0:
            n3 = n3 + num[x]
    print('Somando os valores pares de {}, temos {}'.format(num, n3))


sorte()
soma()
