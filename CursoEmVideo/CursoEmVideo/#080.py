n1 = []
for x in range(0, 5):
    n = int(input('Digite um valor: '))
    if x == 0 or n > n1[-1]:
        n1.append(n)
        print('Adicionando ao final da lista')
    else:
        pos = 0
        while pos < len(n1):
            if n <= n1[pos]:
                n1.insert(pos, n)
                print('Adicionando na posiçao {} da lista'.format(pos))
                break
            pos += 1
print('-=' * 20)
print('Os valores digitados foram: {}'.format(n1))

