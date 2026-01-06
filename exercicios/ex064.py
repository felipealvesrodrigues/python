total = n = cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    total += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma é {}'.format(cont, total)) 

# A maneira errada é subtrair 999 do total e subtrair 1 do contador, pra brular isso, é so por o comando fora do while e colocar o mesmo comando dentro no final do while