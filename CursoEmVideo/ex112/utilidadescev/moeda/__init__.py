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


def resumo(x=0, a=0, d=0):
    print('-' * 30)
    print('       RESUMO DO VALOR')
    print('-' * 30)
    print('Preço analisado:    {}'.format(moeda(x)))
    print('Dobro do preço:     {}'.format(moeda(x * 2)))
    print('Metada do preço:    {}'.format(moeda(x / 2)))
    print('{}% de aumento:     {}'.format(a, moeda(x + (x * a / 100))))
    print('{}% de reduçao:     {}'.format(d, moeda(x - (x * d / 100))))
    print('-' * 30)
