n1 = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print('-' * 30)
print('Voce digitou os valores: {}'.format(n1))
n = n1.count(9)
print('O valor 9 apareceu {} vezes'.format(n))
if 3 in n1:
    print('O valor 3 apareceu na {} posiçao'.format(n1.index(3) + 1))
else:
    print('O valor 3 apareceu nao apareceu')
print('Os valores pares digitados foram: ', end='')
for x in n1:
    if x % 2 == 0:
        print(x, end='')

