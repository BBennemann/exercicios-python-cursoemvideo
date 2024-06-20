print('Gerador de PA')
print('=-' * 10)
c = 1
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razao da PA: '))
while c <= 10:
    print('{} -> '.format(n1), end='')
    n1 = n1 + n2
    c = c + 1
print('FIM')


