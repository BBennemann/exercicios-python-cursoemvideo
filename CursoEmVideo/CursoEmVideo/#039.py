from datetime import date
n4 = int(input('Vc é homem[1] ou mulher[2]? '))
if n4 == 1:
    n1 = int(input('Informe o ano q vc nasceu: '))
    n2 = date.today().year
    n3 = n2 - n1
    print('Quem nasceu em {} tem {} anos em {}'.format(n1, n3, n2))
    if n3 == 18:
        print('Esse ano vc deve se alistar')
    elif n3 > 18:
        print('Vc ja deveria ter se alistado ha {} anos'.format(n3 - 18))
        print('Seu alistamento foi em {}'.format(n1 + 18))
    else:
        print('ainda faltam {} anos para o alistamento'.format(18 - n3))
        print('Seu alistamento sera em {}'.format(n1 + 18))
else:
    print('Voce n precisa se alistar.')







