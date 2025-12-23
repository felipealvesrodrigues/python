""" num = int(input('Digite um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}.'.format(n[3]))
print('Dezena: {}.'.format(n[2]))
print('Centena: {}.'.format(n[1]))
print('Milhar: {}.'.format(n[0]))
 """
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: \033[31m{}\033[m.'.format(u))
print('Dezena: \033[33m{}\033[m.'.format(d))
print('Centena: \033[35m{}\033[m.'.format(c))
print('Milhar: \033[34m{}\033[m.'.format(m))

