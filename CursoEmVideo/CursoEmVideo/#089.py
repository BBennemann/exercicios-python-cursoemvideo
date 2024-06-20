l = []
cont = 1
while True:
    n1 = str(input('Nome: '))
    n2 = float(input('Nota 1: '))
    n3 = float(input('Nota 2: '))
    media = ((n2 + n3) / 2)
    l.append([n1, [n2, n3], media])
    n4 = str(input('Quer continuar? [S/N] ')).upper()
    if n4 == 'N':
        break
    elif n4 == 'S':
        cont += 1
print('-=' * 30)
print('No. NOME       MEDIA')
print('-' * 21)
for x in range(0, cont):
    print('{}     {}         {}'.format(x, l[x][0], l[x][2]))
while True:
    print('-' * 21)
    opc = int(input('Mostrar nota d qual aluno? [999 para]: '))
    if opc == 999:
        break
    if opc <= len(l) - 1:
        print('Notas de {} são {}'.format(l[opc][0], l[opc][1]))
