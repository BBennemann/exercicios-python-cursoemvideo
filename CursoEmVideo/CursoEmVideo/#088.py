from random import randint
j = list()
l = list()
cont = 0
print('-' * 20)
print('JOGUE NA MEGA SENA')
print('-' * 20)
n1 = int(input('Quantos jogos voce quer sortear? '))
for x in range(0, n1):
    cont = 0
    while cont != 6:
        n2 = randint(1, 60)
        if n2 not in j:
            j.append(n2)
            cont += 1
    j.sort()
    l.append(j[:])
    j.clear()
for x in range(0, n1):
    print('Jogo {}: {}'.format(x, l[x]))
