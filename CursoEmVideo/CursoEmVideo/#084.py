t = []
t2 = []
cont = 0
M = m = 0
while True:
    t.append(str(input('Nome: ')).capitalize())
    t.append(float(input('Peso: ')))
    if cont == 0:
        M = m = t[1]
    elif t[1] > M:
        M = t[1]
    elif t[1] < m:
        m = t[1]
    cont += 1
    t2.append(t[:])
    t.clear()
    c = str(input('Quer continuar? [S/N] ')).upper()
    if c == 'N':
        break
print('-=' * 20)
print('Ao todo, voce cadastrou {} pessoas'.format(cont))
print('O maior peso foi {} kg. Peso de '.format(M), end='')
for p in t2:
    if p[1] == M:
        print(f'[{p[0]}]', end=' ')
print()
print('O menor peso foi {} kg. Peso de '.format(m), end='')
for p in t2:
    if p[1] == m:
        print(f'[{p[0]}]', end=' ')