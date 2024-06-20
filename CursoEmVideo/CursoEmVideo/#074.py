from random import randint
n1 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for x in n1:
    print('{} '.format(x), end='')
print('\nO maior valor sorteado foi {}'.format(max(n1)))
print('O menor valor sorteado foi {}'.format(min(n1)))



