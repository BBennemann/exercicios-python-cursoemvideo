from random import randint
print('Vou pensar em um numero de 1 a 5 tente advinhar')
n1 = int(input('Em qual numero eu pensei: '))
n = randint(1, 5)
if n1 == n:
    print('parabens voce acertou')
else:
    print('ah q pena vc errou')
print('meu numero era {}'.format(n))
