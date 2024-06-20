from datetime import date
n1 = int(input('Ano de nascimento: '))
n2 = date.today().year
n3 = n2 - n1
if 0 < n3 <= 9:
    print('Mirim')
elif 9 < n3 <= 14:
    print('Infantil')
elif 14 < n3 <= 19:
    print('Junior')
elif 19 < n3 <= 25:
    print('Senior')
else:
    print('Master')




