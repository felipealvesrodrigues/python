import random
from time import sleep
n = random.randint(0, 5)
g = int(input('Chute um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if g == n:
    print('Parabéns!! Você acertou :)')
else:
    print('Errou feio filho >:(')
