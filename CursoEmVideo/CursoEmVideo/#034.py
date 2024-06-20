n1 = float(input('Qual é o salario do funcionario? R$'))
if n1 > 1250:
    n2 = n1 * 10 / 100 + n1
else:
    n2 = n1 * 15 / 100 + n1
print('O salario dps do aumento é de {}'.format(n2))

