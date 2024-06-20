inf = {}
inf['nome'] = str(input('Nome: ')).capitalize()
n = int(input('Ano de nascimento: '))
inf['idade'] = 2021 - n
inf['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if inf['ctps'] == 0:
    print('-=' * 25)
    for k, i in inf.items():
        print('- {} tem o valor de {}'.format(k, i))
else:
    inf['contratação'] = int(input('Ano de contratação: '))
    inf['salario'] = float(input('Salario: R$'))
    inf['aposentadoria'] = inf['contratação'] + 35 - n
    print('-=' * 25)
    for k, i in inf.items():
        print('- {} tem o valor de {}'.format(k, i))
