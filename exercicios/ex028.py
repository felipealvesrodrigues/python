import random
from time import sleep
n = random.randint(0, 5)
g = int(input('Chute um número de 0 a 5: '))
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if g == n:
    print('\033[4;32mParabéns!! Você acertou :)\033[m')
else:
    print('\033[4;31mErrou feio filho >:(\033[m')
