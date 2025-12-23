frase = str(input('Digite uma frase: ')).strip().lower()
print('letra A aparece \033[34m{}\033[m vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição \033[41m{}\033[m'.format(frase.find('a')+1)) # so pra ao invés de mostrar 0, mostrar 1
print('A última letra A apareceu na posição \033[45m{}\033[m'.format(frase.rfind('a')+1))