n = input('Digite seu nome completo: ').strip()
n1 = n.split()
print('seu em maiusculo é {}'.format(n.upper()))
print('seu nome em minusculo é {}'.format(n.lower()))
print('seu nome tem {} letras'.format(len(n) - n.count(' ')))
#print('seu primeiro nome tem {} letras'.format(n.find(' ')))
print('seu primeiro nome tem {} letras'.format(len(n1[0])))

