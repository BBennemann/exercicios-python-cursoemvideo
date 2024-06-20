s = 0
for x in range(1, 7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        s = s + n1
print('A soma dos pares é {}'.format(s))
