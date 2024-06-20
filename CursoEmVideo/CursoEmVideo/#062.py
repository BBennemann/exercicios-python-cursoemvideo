print('Gerador de PA')
print('=-' * 10)
c = 1
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razao da PA: '))
n3 = 10
n4 = 0
while n3 != 0:
    n4 = n4 + n3
    while c <= n4:
        print('{} -> '.format(n1), end='')
        n1 = n1 + n2
        c = c + 1
    print('PAUSE')
    n3 = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(n4))
