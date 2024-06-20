def leiaint(x):
    while True:
        try:
            n1 = int(input(x))
        except:
            print('\033[0;31mERRO! Digite um numero inteiro valido\033[m')
            print('-' * 42)
        else:
            print('-' * 42)
            return n1


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

