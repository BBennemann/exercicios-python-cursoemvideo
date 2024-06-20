l =[[], [], []]
for x in range(0, 3):
    l[0].append(int(input('Digite um valor para [0, {}]: '.format(x))))
for x in range(0, 3):
    l[1].append(int(input('Digite um valor para [1, {}]: '.format(x))))
for x in range(0, 3):
    l[2].append(int(input('Digite um valor para [2, {}]: '.format(x))))
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
