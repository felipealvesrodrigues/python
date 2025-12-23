nome = input('Digite seu nome: ')
upper = nome.upper()
lower = nome.lower()
sem_espaço = nome.replace(" ", "")
total = len(sem_espaço)
separar = nome.split()
primeiro_nome = len(separar[0])
print('Maiúsculas: \033[1;31m{}\033[m.\nMinúsculas: \033[33m{}\033[m.\nTotal de letras \033[1;35m{}\033[m.\nPrimeiro Nome: \033[1;36m{}\033[m letras. '.format(upper, lower, total, primeiro_nome))


