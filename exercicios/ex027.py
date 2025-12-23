nome = str(input('Digite sue nome completo: ')).strip()
dividir = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é \033[32;42m{}\033[m\nSeu último nome é \033[31m{}\033[m'.format(dividir[0], dividir[-1]))