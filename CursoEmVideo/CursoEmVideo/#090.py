inf = {}
inf['nome'] = str(input('Nome do aluno: ')).capitalize()
inf['media'] = int(input('Media do aluno: '))
# Serve pra msm coisa q os 2 print embaixo
# for k, v in inf.items():
#     print('{} = {}'.format(k, v))
print('Nome = {}'.format(inf['nome']))
print('Media = {}'.format(inf['media']))
if inf['media'] >= 7:
    print('Situaçao = \033[0;32mAprovado\033[m')
elif inf['media'] >= 5:
    print('Situação = \033[0;33mRecuperação\033[m')
else:
    print('Situação = \033[0;31mReprovado\033[m')
