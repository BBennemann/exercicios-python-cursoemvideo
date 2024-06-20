from ex107 import moeda
n1 = float(input('Digite o preço: R$'))
print(f'A metade de R${n1} é R${moeda.metade(n1)}')
print(f'O dobro de R${n1} é R${moeda.dobro(n1)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n1)}')
print(f'Diminuido 10%, temos R${moeda.diminuir(n1)}')
