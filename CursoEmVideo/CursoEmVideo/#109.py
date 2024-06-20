from ex109 import moeda

n1 = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n1)} é {moeda.metade(n1, True)}')
print(f'O dobro de {moeda.moeda(n1)} é {moeda.dobro(n1, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n1, True)}')
print(f'Diminuido 10%, temos {moeda.diminuir(n1, True)}')