n1 = int(input('Digite um numero inteiro: '))
print('Escolha \033[0;35mUMA\033[m das bases para conversao: ')
print('[1] para \033[0;31mBINARIO\033[m')
print('[2] para \033[0;34mOCTAl\033[m')
print('[3] para \033[0;33mHEXADECIMAL\033[m')
n2 = int(input('Sua opçao: '))
if n2 == 1:
    print('{} convertido para \033[0;31mBINARIO\033[m é {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('{} convertido para \033[0;34mOCTAl\033[m é {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('{} convertido para \033[0;33mHEXADECIMAL\033[m é {}'.format(n1, hex(n1)[2:]))





