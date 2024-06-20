n1 = []
while True:
    n = (int(input('Digite um numero: ')))
    if n not in n1:
        n1.append(n)
    else:
        print('Repetido n pd')
    n2 = str(input('Voce quer continuar? [S/N] ')).upper()
    if n2 == 'N':
        break
    elif n2 != 'S':
        n2 = str(input('Invalido, voce quer continuar? [S/N] ')).upper()
n1.sort()
print('Voce digitou os numeros: {}'.format(n1))
