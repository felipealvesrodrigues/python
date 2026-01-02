n = str(input('Qual seu sexo? [M/F] ')).upper()
while n != 'M' and n != 'F': # podia usar while n != 'mmFf'
    print('tente novamente')
    n = str(input('Qual seu sexo? [M/F] ')).upper()
print('Fim')