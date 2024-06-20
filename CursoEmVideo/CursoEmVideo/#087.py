l =[[], [], []]
p = m = 0
for x in range(0, 3):
    l[0].append(int(input('Digite um valor para [0, {}]: '.format(x))))
    if l[0][x] % 2 == 0:
        p = p + l[0][x]
for x in range(0, 3):
    l[1].append(int(input('Digite um valor para [1, {}]: '.format(x))))
    if x == 0:
        m = l[1][x]
    elif l[1][x] > m:
        m = l[1][x]
    if l[1][x] % 2 == 0:
        p = p + l[1][x]
for x in range(0, 3):
    l[2].append(int(input('Digite um valor para [2, {}]: '.format(x))))
    if l[2][x] % 2 == 0:
        p = p + l[2][x]
print('-=' * 30)
for x in range(0, 3):
    print('[{:^5}]'.format(l[0][x]), end='')
print()
for x in range(0, 3):
    print('[{:^5}]'.format(l[1][x]), end='')
print()
for x in range(0, 3):
    print('[{:^5}]'.format(l[2][x]), end='')
print()
print('-=' * 30)
print('A soma dos valores pares é {}'.format(p))
print('A soma da terceira coluna é {}'.format(l[0][2] + l[1][2] + l[2][2]))
print('O maior valor da segunda linha é {}'.format(m))
