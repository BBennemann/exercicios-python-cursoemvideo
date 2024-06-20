n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('Digite um numero entre 0 e 20: '))
    if n1 < 0 or n1 > 20:
        n1 = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
        if n1 >= 0 and n1 <= 20:
            print('Voce digitou o nemero {}'.format(n[n1]))
            n2 = str(input('Voce quer continuar? [S/N]')).upper()[0]
            if n2 == 'N':
                break
    elif n1 >= 0 and n1 <= 20:
        print('Voce digitou o nemero {}'.format(n[n1]))
        n2 = str(input('Voce quer continuar? [S/N]')).upper()[0]
        if n2 == 'N':
            break
print('Fim do programa')
