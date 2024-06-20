n1 = float(input('Qual o seu peso? (Kg)'))
n2 = float(input('Qual a sua altura? (m)'))
n3 = n1 / n2 ** 2
print(n3)
if n3 <= 18.5:
    print('Abaixo do peso')
elif n3 <= 25:
    print('Ta no peso ideal')
elif n3 <= 30:
    print('Sobrepeso')
elif n3 <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')



