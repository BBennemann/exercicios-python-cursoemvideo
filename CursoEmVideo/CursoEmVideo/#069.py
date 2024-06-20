print('-' * 20)
print('    CADASTRE UMA PESSOA')
print('-' * 20)
d = 0
h = 0
m = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        d = d + 1
    sexo = str(input('Sexo: [M/F] ')).upper()
    if sexo == 'M':
        h = h + 1
    elif sexo == 'F' and idade <= 20:
        m = m + 1
    print('-' * 20)
    n1 = str(input('Quer continuar? [S/N] ')).upper()[0]
    if n1 == 'N':
        print('-' * 20)
        break
    elif n1 == 'S':
        print('-' * 20)
print('Total de pessoa com mais de 18 anos: {}'.format(d))
print('Ao todo temos {} homens cadastrados'.format(h))
print('E temos {} mulher com menos de 20 anos'.format(m))

