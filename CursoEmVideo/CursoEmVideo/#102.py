def fatorial(n, show=False):
    f = 1
    for x in range(n, 0, -1):
        if show:
            print(x, end='')
            if x > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= x
    return f


n1 = int(input('Qual numero vc quer ver o fatorial: '))
n2 = str(input('Quer ver o calculo? [S/N] ')).upper()[0]
if n2 in 'Ss':
    print(fatorial(n1, show=True))
else:
    print(fatorial(n1, show=False))
