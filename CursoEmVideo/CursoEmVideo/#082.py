n1 = []
p = []
i = []
cont = 0
while True:
    n = int(input('Digite um numero: '))
    n1.append(n)
    if n1[cont] % 2 == 0:
        p.append(n)
    elif n1[cont] % 2 == 1:
        i.append(n)
    cont += 1
    n2 = str(input('Voce quer continuar? [S/N] ')).upper()
    if n2 == 'N':
        break
    elif n2 != 'S':
        n2 = str(input('Invalido, voce quer continuar? [S/N] ')).upper()
print('A lista completa é {}'.format(n1))
print('A lista de pares é {}'.format(p))
print('A lista de impares é {}'.format(i))

