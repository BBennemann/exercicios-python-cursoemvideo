n1 = str(input('Digite uma frase: ')).upper().strip()
s = n1.split()
n2 = ''.join(s)
n3 = n2[::-1]
print('A frase {} ao contrario é {}'.format(n2, n3))
if n2 == n3:
    print('Temos um Palindromo')
else:
    print('A frase n é um palindromo')
