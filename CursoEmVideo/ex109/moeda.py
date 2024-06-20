def dobro(x=0, y=False):
    x = x * 2
    return x if y is False else moeda(x)


def metade(x=0, y=False):
    x = x / 2
    return x if y is False else moeda(x)


def aumentar(x=0, y=False):
    x2 = x * 10 / 100
    x += x2
    return x if y is False else moeda(x)


def diminuir(x=0, y=False):
    x2 = x * 10 / 100
    x -= x2
    return x if y is False else moeda(x)


def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')
