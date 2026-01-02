import random
from time import sleep
n = random.randint(0, 10)
g = int(input('Chute um número de 0 a 10: '))
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
t = 1
while g != n:
    print('tente novamente!')
    g = int(input('Chute um número de 0 a 10: '))
    t += 1
print('Parabens! Você tentou {} vezes!'.format(t))
