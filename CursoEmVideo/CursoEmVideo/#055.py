l = 0
p = 0
for x in range(1, 6):
    n1 = float(input('Peso da {}° pessoa: '.format(x)))
    if x == 1:
        l = n1
        p = n1
    else:
        if n1 > p:
            p = n1
        elif n1 < l:
            l = n1
print('O maior peso lido foi de {}Kg'.format(p))
print('O menor peso lido foi de {}Kg'.format(l))
