import math
n2 = float(input('Digite um numero: '))
n1 = math.radians(n2)
s = math.sin(n1)
c = math.cos(n1)
t = math.tan(n1)
print('o sen de {:.2f} é igual a {:.2f}'.format(n2, s))
print('o cos de {} é igual a {:.2f}'.format(n2, c))
print('a tg de {} é igual a {:.2f}'.format(n2, t))
