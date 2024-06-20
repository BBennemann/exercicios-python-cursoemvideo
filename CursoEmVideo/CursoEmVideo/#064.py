n1 = 0
s = 0
c = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]: '))
    s = s + n1
    c = c + 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(c - 1, s - 999))


