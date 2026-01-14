""" print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor 
ced = 50
totced = 0 
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break """
            
            
            
            
            
print('=' * 30)
print('{:^30}'.format('BANCO FAR'))
print('=' * 30)
valor = int(input('Digite um valor para sacar: R$'))
cedula = 50
total_cedulas = 0
while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else: 
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédula(s) de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0 
        if valor == 0:
            break
        
