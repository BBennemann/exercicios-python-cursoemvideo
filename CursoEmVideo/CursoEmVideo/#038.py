n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro valor é \033[0;31mMAIOR\033[m')
elif n2 > n1:
    print('O segundo valor é \033[0;34mMAIOR\033[m')
else:
    print('Os dois valores sao \033[0;32mIGUAIS\033[m')







