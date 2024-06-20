t = [[], []]
v = 0
for x in range(1, 8):
    v = int(input(f'Digite o {x}° valor: '))
    if v % 2 == 0:
        t[0].append(v)
    elif v % 2 == 1:
        t[1].append(v)
print('-=' * 20)
t[0].sort()
print('Os valores pares digitados foram: {}'.format(t[0]))
t[1].sort()
print('Os valores impares digitados foram: {}'.format(t[1]))
