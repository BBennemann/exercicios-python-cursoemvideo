print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n1 = int(input('Quantos termos voce quer mostrar? '))
c = 3
n2 = 0
n3 = 1
print('{} -> {} -> '.format(n2, n3), end='')
while c <= n1:
    n4 = n2 + n3
    print('{} -> '.format(n4), end='')
    c = c + 1
    n2 = n3
    n3 = n4
print('FIM')
