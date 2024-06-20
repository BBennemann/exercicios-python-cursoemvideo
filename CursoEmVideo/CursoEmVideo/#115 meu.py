def titulo():
    print('-' * 35)
    print('          MENU PRINCIPAL')
    print('-' * 35)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 35)


def op(x):
    print('-' * 35)
    print(x)
    print('-' * 35)


while True:
    titulo()
    try:
        n1 = int(input('Sua Opção: '))
        if n1 == 1:
            op('          \033[0;32m   Opção 1\033[m')
        elif n1 == 2:
            op('          \033[0;32m   Opção 2\033[m')
        elif n1 == 3:
            op('          \033[0;32m   Opção 3\033[m')
        else:
            print('\033[0;31mERRO! Digite uma opção valida\033[m')
    except:
        print('\033[0;31mERRO! por favor, digite um numero inteiro valido\033[m')
