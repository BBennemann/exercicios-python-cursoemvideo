print('=' * 26)
print('   10 TERMOS DE UMA PA   ')
print('=' * 26)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
decimo = n1 + (10 - 1) * n2
for x in range(n1, decimo + n2, n2):
    print(x, end='->')
print('ACABOU')
