n = int(input('Digite um valor: '))
a = n - 1
s = n + 1
print('O antecessor de \033[4;36m{}\033[m é \033[4;35m{}\033[m e seu sucessor é \033[4;35m{}'.format(n, a, s))
""" podia ser escrito assim: print('analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n-2))) """