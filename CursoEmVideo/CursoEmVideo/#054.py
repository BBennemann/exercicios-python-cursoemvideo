from datetime import date
v = 0
n = 0
n2 = date.today().year
for x in range(1, 8):
    n1 = int(input('Em que ano a {}° pessoa nasceu? '.format(x))) 
    n3 = n2 - n1
    if n3 >= 18:
        v = v + 1
    else:
        n = n + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(v))
print('E tambem tivemos {} pessoas menores de idade'.format(n))
