print('-' * 20)
print('LOJA SUPER BARATAO')
print('-' * 20)
t = 0
m = 0
b = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while True:
    n = str(input('Nome do produto: '))
    p = int(input('Preço: R$'))
    if p <= b:
        bn = n
        b = p
    t = t + p
    if p >= 1000:
        m = m + 1
    c = str(input('Quer continuar? [S/N] ')).upper()[0]
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper()[0]
    if c == 'N':
        print('-------- FIM DO PROGRAMA --------')
        break
print('O total da compra foi {:.2f}'.format(t))
print('Temos {} produtos custando mais de R$1000.00'.format(m))
print('O produto mais barato foi {} que custou {:.2f}'.format(bn, b))
