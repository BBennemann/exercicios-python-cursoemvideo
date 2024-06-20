s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s != 'M' and s != 'F':
    s = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(s))
