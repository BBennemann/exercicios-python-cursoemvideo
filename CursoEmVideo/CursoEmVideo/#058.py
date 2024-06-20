from random import randint
cont = 0
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
n1 = randint(0, 10)
print('Sera q vc consegue advinhar qual foi?')
n = 11
while n != n1:
    n = int(input('Qual seu palpite? '))
    cont = cont + 1
    if n > n1:
        print('Menos... Tente mais uma vez')
    elif n < n1:
        print('Mais... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(cont))
