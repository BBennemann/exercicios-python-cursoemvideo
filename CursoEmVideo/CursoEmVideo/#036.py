n1 = float(input('Qual o valor da casa? '))
n2 = float(input('Qual o seu salario salario? '))
n3 = int(input('Em quantos anos pretende pagar? '))
n4 = n1 / n3 / 12
n5 = n2 * 30 / 100
print('A prestaçao mensal é de {:.2f}'.format(n4))
if n4 > n5:
    print('Emprestimo \033[0;31mNEGADO\033[m')
else:
    print('Emprestimo \033[0;32mAPROVADO\033[m')


