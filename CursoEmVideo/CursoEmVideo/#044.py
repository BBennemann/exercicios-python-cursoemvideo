n1 = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''[1] a vista dinheiro/cheque
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
n2 = int(input('Qual a opçao? '))
if n2 == 1:
    print('Pagando a vista no dinheiro ou cheque voce ganha 10% de desconto ficando {}R$'.format(n1 * 90 / 100))
elif n2 == 2:
    print('Pagando a vista no cartao voce ganha 5% de desconto ficando {}R$'.format(n1 * 95 / 100))
elif n2 == 3:
    print('Pagando 2x no cartao o preço continua igual ficando {}R$'.format(n1))
elif n2 == 4:
    print('pagando 3x ou mais no cartao voce ganha 20% de juros ficando {}R$'.format(n1 + n1 * 20 / 100))
else:
    print('Opçao invalida de pagamento tente novamente')






