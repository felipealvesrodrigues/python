s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('\033[32mUm triângulo pode ser fomado!\033[m')
else: 
    print('\033[31mUm triângulo não pode ser formado\033[m')

