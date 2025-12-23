""" nome = input('Qual seu nome?')
print('É um prazer te conhecer', nome) """

nome = input('\033[4;37;43mQual seu nome?\033[m')
print('É um prazer te conhecer, \033[7;30m{}!' .format(nome))
