cont = 0
n1 = 0
n2 = 0
while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    n2 = n2 + n1
    cont = cont + 1
print('A soma dos {} valores foi {}'.format(cont, n2))

