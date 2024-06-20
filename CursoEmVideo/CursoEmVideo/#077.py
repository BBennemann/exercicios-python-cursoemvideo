p = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for x in p:
    print('\nNa palavra {} temos: '.format(x.upper()), end='')
    for l in x:
        if l in 'aeiou':
            print(l.upper(), end=' ')