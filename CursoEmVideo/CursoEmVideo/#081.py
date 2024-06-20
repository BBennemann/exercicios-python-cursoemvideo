n1 = []
while True:
    n1.append((int(input('Digite um numero: '))))
    n2 = str(input('Voce quer continuar? [S/N] ')).upper()
    if n2 == 'N':
        break
    elif n2 != 'S':
        n2 = str(input('Invalido, voce quer continuar? [S/N] ')).upper()
print('=-' * 20)
n1.sort(reverse = True)
print('Foram digitados {} valores'.format(len(n1)))
print('Em ordem decrescente {}'.format(n1))
if 5 in n1:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 n esta na lista')



