v = 0
h = 0
m = 0
mi = 0
for x in range(1, 5):
    print('------- {}° pessoa -------'.format(x))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    mi = mi + i
    s = str(input('Sexo [M/F]: ')).upper()
    if 'F' in s:
        if i <= 20:
            m = m + 1
    elif 'M' in s:
        h = h + 1
        if h == 1:
            v = i
        elif v < i:
            v = i
            n1 = n[:]
print('A media de idade do grupo é de {} anos'.format(mi / 5))
print('O homem mais velho tem {} anos e se chama {}'.format(v, n1))
print('Ao todo são {} mulheres com menos de 20 anos'.format(m))
