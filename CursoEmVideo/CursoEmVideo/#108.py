from ex108 import moeda

n1 = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n1)} é {moeda.moeda(moeda.metade(n1))}')
print(f'O dobro de {moeda.moeda(n1)} é {moeda.moeda(moeda.dobro(n1))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(n1))}')
print(f'Diminuido 10%, temos {moeda.moeda(moeda.diminuir(n1))}')
