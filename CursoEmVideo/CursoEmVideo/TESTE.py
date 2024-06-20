from random import randint

linha1 = dict(n1=0, n2=0, n3=0)
linha2 = dict(n1=0, n2=0, n3=0)
linha3 = dict(n1=0, n2=0, n3=0)

while linha1['n1'] + linha1['n2'] + linha1['n3'] != 21:
    linha1['n1'] = randint(1, 10)
    linha1['n2'] = randint(1, 10)
    linha1['n3'] = randint(1, 10)

while linha1['n1'] + linha2['n1'] + linha3['n1'] != 21:
    linha2['n1'] = randint(1, 10)
    linha3['n1'] = randint(1, 10)

while linha3['n1'] + linha3['n2'] + linha3['n3'] != 21:
    linha3['n2'] = randint(1, 10)
    linha3['n3'] = randint(1, 10)

while linha1['n3'] + linha2['n3'] + linha3['n3'] != 21:
    linha2['n3'] = randint(1, 10)

#while linha2['n1'] + linha2['n2'] + linha2['n3'] != 21:
#    linha2['n2'] = randint(1, 10)

#while linha1['n2'] + linha2['n2'] + linha3['n2'] != 21:
#    linha2['n2'] = randint(1, 10)


print(linha1['n1'], 'z', linha1['n3'])
print('z', 'x', 'z')
print(linha3['n1'], 'z', linha3['n3'])

resp = int(input("sabendo que os lados do quadrado valem 21 e \nque x é igual a soma de seus adjacentes, quanto vale x? "))

while not resp == linha1['n2'] + linha2['n1'] + linha2['n3'] + linha3['n2']:
    resp = int(input('Tenta dnvo: '))
else:
    print('Parabens vc acertou!!')