import math
n1 = float(input('comprimento do cateto oposto: '))
n2 = float(input('ocmprimento do cateto adjacente: '))
h = math.hypot(n1, n2)
print('a hipotenusa vai medir {:.2f}'.format(h))
