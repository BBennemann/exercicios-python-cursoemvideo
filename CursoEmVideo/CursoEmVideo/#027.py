n = str(input('Digite seu nome completo: ')) .strip()
n1 = n.split()
print('Seu primeiro nome é {}'.format(n1[0]))
print('seu ultimo nome é {}'.format(n1[len(n1)-1]))

