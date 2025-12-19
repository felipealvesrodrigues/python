nome = str(input('Digite sue nome completo: ')).strip()
dividir = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(dividir[0], dividir[-1]))