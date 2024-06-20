n1 = []
maior = 0
menor = 0
for x in range(0, 5):
    n1.append(int(input('Digite o numero {}: '.format(x))))
    if x == 0:
        maior = n1[x]
        menor = n1[x]
    elif maior < n1[x]:
        maior = n1[x]
    elif menor > n1[x]:
        menor = n1[x]
print('=-'*20)
print('Voce digitou os valores: {}'.format(n1))
print('O maior valor digitado foi {} nas posiçoes '.format(maior), end='')
for i, v in enumerate(n1):
    if v == maior:
        print('{}... '.format(i), end='')
print()
print('O menor valor digitado foi {} nas posiçoes '.format(menor), end='')
for i, v in enumerate(n1):
    if v == menor:
        print('{}... '.format(i), end='')
