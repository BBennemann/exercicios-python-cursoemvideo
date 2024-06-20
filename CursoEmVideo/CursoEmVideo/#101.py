def voto(x):
    from datetime import date
    n2 = date.today().year - n1
    if 18 <= x <= 70:
        return 'Com {} anos: VOTO OBRIGATORIO.'.format(n2)
    elif 16 <= x <= 17 or x > 70:
        return 'Com {} anos: VOTO OPCIONAL.'.format(n2)
    elif x < 16:
        return 'Com {} anos: NÃO VOTA '.format(n2)


print('-' * 25)
n1 = int(input('Em que ano voce nasceu? '))
print('-' * 25)
print(voto(n1))
