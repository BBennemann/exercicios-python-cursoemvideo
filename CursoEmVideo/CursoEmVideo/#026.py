n1 = input('Digite uma frase: ').strip() .lower()
print('a letra A apareceu {} vezes'.format(n1.count('a')))
print('a primeira letra A apareceu na posiçao {}'.format(n1.find('a')+1))
print('a ultima letra A aparece na posiçao {}'.format(n1.rfind('a')+1))


