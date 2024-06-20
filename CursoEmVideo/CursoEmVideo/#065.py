q = 's'
s = 0
c = 0
M = 0
m = 999
while q == 's':
    n1 = int(input('Digite um numero: '))
    s = s + n1
    q = str(input('Quer continuar? [S/N] ')).lower()
    if c == 0:
        M = n1
        m = n1
    else:
        if M < n1:
            M = n1
        elif m > n1:
            m = n1
    c = c + 1
print('Voce digitou {} numeros e a media entre eles é {:.2f}'.format(c, s / c))
print('O maior numero é {} e o menor é {}'.format(M, m))
