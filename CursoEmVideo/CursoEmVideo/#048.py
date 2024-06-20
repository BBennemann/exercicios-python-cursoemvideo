s = 0
c = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        c = c + 1
        s = s + x
print('A soma d todos os {} valores é {}'.format(c, s))
