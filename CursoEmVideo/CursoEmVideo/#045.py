from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opçoes:
[0] \033[0;35mpedra\033[m
[1] \033[0;97mpapel\033[m
[2] \033[0;33mtesoura\033[m''')
n1 = int(input('Escolha uma: '))
n2 = randint(0, 2)
print('''---------------------------------
O computador jogou {}
O player jogou {}
---------------------------------'''.format(itens[n2], itens[n1]))
if n1 == 0 and n2 == 0:
    print('\033[0;34mEMPATE')
elif n1 == 0 and n2 == 1:
    print('\033[0;31mCOMPUTADOR WINS')
elif n1 == 0 and n2 == 2:
    print('\033[0;32mPLAYER WINS')
#------------------------------------------------------------
if n1 == 1 and n2 == 0:
    print('\033[0;32mPLAYER WINS')
elif n1 == 1 and n2 == 1:
    print('\033[0;34mEMPATE')
elif n1 == 1 and n2 == 2:
    print('\033[0;31mCOMPUTADOR WINS')
#----------------------------------------------------------
if n1 == 2 and n2 == 0:
    print('\033[0;31mCOMPUTADOR WINS')
elif n1 == 2 and n2 == 1:
    print('\033[0;32mPLAYER WINS')
elif n1 == 2 and n2 == 2:
    print('\033[0;34mEMPATE')





