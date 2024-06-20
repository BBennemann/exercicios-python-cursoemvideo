def leiadinheiro(x):
    while True:
        n = str(input(x)).replace(',', '.').strip()
        if n.isalpha() or n == '' or n.isalnum():
            print('\033[0;31mERRO! "{}" não é um numero valido, só numeros por favor\033[m'.format(n))
        else:
            return float(n)
            break
