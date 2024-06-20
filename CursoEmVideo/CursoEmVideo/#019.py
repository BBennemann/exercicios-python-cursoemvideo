from random import choice
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
l = [n1, n2, n3, n4]
r = choice(l)
print('o aluno escolhido foi {}'.format(r))
