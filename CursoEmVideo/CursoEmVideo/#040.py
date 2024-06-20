n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = (n1 + n2) / 2
print('Tirando {} e {}, a media do aluno é {:.1f}'.format(n1, n2, n3))
if 5 < n3 <= 7:
    print('O aluno esta de \033[0;31mRECUPERÇAO\033[m')
elif n3 <= 5:
    print('o aluno esta REPROVADO')
else:
    print('O aluno esta \033[0;32mAPROVADO\033[m')







