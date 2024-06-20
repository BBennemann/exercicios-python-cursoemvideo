from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
cont = 0
while True:
    c = randint(0, 10)
    n1 = int(input('Diga um valor: '))
    n2 = str(input('Par ou Imapar [P/I]: ')).upper()[0]
    print('-' * 25)
    t = (c + n1) % 2
    if t == 1:
        print('Voce jogou {} e o computador {}. total de {} DEU IMPAR'.format(n1, c, n1 + c))
        print('-' * 25)
    elif t == 0:
        print('Voce jogou {} e o computador {}. total de {} DEU PAR'.format(n1, c, n1 + c))
        print('-' * 25)
    if n2 == 'I' and t == 1 or n2 == 'P' and t == 0:
        cont = cont + 1
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    elif n2 == 'I' and t == 0 or n2 == 'P' and t == 1:
        print('Voce PERDEU!')
        print('=-' * 20)
        break
print('GAME OVER! Voce venceu {} vezes'.format(cont))
