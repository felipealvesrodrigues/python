n = int(input('Digite um valor: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de \033[34;43m{}\033[m é \033[1;36;44m{}\033[m, o triplo é \033[1;36;44m{}\033[m e a raiz quadrada é \033[1;36;44m{:.3f}\033[m'.format(n, d, t, r))