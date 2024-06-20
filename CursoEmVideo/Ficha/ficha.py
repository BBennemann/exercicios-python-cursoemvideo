def dado(x):
    from random import randint
    ndado = randint(1, 100)
    print(ndado)
    if ndado <= x / 5:
        return '\033[0;32mEXTREMO\033[m'
    elif ndado <= x / 2:
        return '\033[0;34mBOM\033[m'
    elif ndado <= x:
        return 'NORMAL'
    elif ndado < 95:
        return '\033[0;33mFALHA\033[m'
    else:
        return '\033[0;31mDESASTRE\033[m'


print(dado(30))


#  while True:
#    from random import randint
#    dado = int(input('Numero do dado: '))
#    pericia = int(input('Pontos na pericia: '))
#    ndado = randint(1, dado)
#    print(ndado)
#    if ndado <= pericia / 5:
#        print('EXTREMO')
#    elif ndado <= pericia / 2:
#        print('BOM')
#    elif ndado <= pericia:
#        print('NORMAL')
#    elif ndado < 95:
#        print('FALHA')
#    else:
#        print('DESASTRE')
