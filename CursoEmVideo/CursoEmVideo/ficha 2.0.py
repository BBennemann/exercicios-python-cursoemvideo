from Ficha import ficha

Dallan = dict()

Dallan['for'] = 30
Dallan['des'] = 70
Dallan['con'] = 40
Dallan['car'] = 70
Dallan['int'] = 40
Dallan['exp'] = 20
Dallan['sor'] = 70
Dallan['pod'] = 20

print('pos  atributo      num')
print('=-' * 12)
n = 0
for k, i in Dallan.items():
    n += 1
    print(f' {n}     {k}  ---->  {i}')
print('=-' * 20)

while True:
    n1 = str(input('nome do atributo que quer rolar: '))
    if n1 == 'for':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'des':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'con':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'car':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'int':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'exp':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'sor':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
    elif n1 == 'pod':
        print(ficha.dado(Dallan[n1]))
        print('=-' * 20)
