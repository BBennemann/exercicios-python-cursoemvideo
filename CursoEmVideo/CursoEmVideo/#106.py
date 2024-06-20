def ajuda(x):
    help(x)


while True:
    n1 = str(input('Funçao ou biblioteca > ')).lower()
    if n1 == 'fim':
        break
    else:
        ajuda(n1)
