def dobro(x = 0):
    x = x * 2
    return x


def metade(x = 0):
    x = x / 2
    return x


def aumentar(x = 0):
    x2 = x * 10 / 100
    x += x2
    return x


def diminuir(x = 0):
    x2 = x * 10 / 100
    x -= x2
    return x


def moeda(x = 0, moeda = 'R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')
