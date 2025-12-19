nome = input('Digite seu nome: ')
upper = nome.upper()
lower = nome.lower()
sem_espaço = nome.replace(" ", "")
total = len(sem_espaço)
separar = nome.split()
primeiro_nome = len(separar[0])
print('Maiúsculas: {}.\nMinúsculas: {}.\nTotal de letras {}.\nPrimeiro Nome: {} letras. '.format(upper, lower, total, primeiro_nome))


