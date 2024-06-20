def leiaint():
    while True:
        try:
            n1 = int(input('Digite um Inteiro: '))
        except:
            print('\033[0;31mERRO! Digite um numero inteiro valido\033[m')
            print('-' * 20)
        else:
            print('-' * 20)
            break

while True:
    try:
        n2 = float(input('Digite um Real: '))
    except:
        print('\033[0;31mERRO! Digite um numero real valido\033[m')
        print('-' * 20)
    else:
        print('-' * 20)
        break

print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

