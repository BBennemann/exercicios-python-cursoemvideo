tudo = []
pessoas = {}
m = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    s = str(input('Sexo: [M/F] ')).upper()
    while s != 'F' and s != 'M':
        print('ERRO! Responda apenas M ou F.')
        s = str(input('Sexo: [M/F] '))[0].upper()
    pessoas['sexo'] = s
    i = int(input('Idade: '))
    m += i
    pessoas['idade'] = i
    tudo.append(pessoas.copy())
    n = str(input('Quer continuar? [S/N] '))[0].upper()
    while n != 'S' and n != 'N':
        print('ERRO! Responda apenas S ou N.')
        n = str(input('Quer continuar? [S/N] '))[0].upper()
    if n == 'N':
        break
print('-=' * 30)
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(tudo)))
print('B) A media de idade é de {:.2f} anos.'.format(m / len(tudo)))
print('C) As mulheres cadastradas foram ', end='')
for p in tudo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) As pessoas acima da media de idade são ', end='')
for p in tudo:
    if p['idade'] >= (m / len(tudo)):
        print('    ')
        for k, i in p.items():
            print('{} = {}; '.format(k, i), end='')
        print()
print('<< ENCERRADO >>')
