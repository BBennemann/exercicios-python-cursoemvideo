p = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('-' * 30)
print('      LISTAGEM DE PREÇO')
print('-' * 30)
for x in range(0, len(p)):
    if x % 2 == 0:
        print('{:.<22}'.format(p[x]), end='')
    else:
        print('R${:>6.2f}'.format(p[x]))
