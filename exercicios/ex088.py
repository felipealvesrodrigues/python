""" era pra usar list(), mas ?????????????
import random
quantos= int(input('Quantos jogos você quer que eu sorteie? '))
for jogo in range(1, quantos + 1):
    sorteio= random.sample(range(0, 61), 6)
    sorteio.sort()
    print(f'Jogo {jogo}: {sorteio}') """
    
# MEU
import random
megasena= list()
quantos= int(input('Quantos jogos você quer que eu sorteie? '))
for jogos in range(0, quantos):
    sorteio= random.sample(range(1, 61), 6)
    sorteio.sort()
    megasena.append(sorteio[:])
    sorteio.clear()
for c, numero in enumerate(megasena):
    print(f'Jogo {c+ 1}: {numero}')

    
# GUANABARA
""" from random import randint
from time import sleep
lista= list()
jogos= list()
print('-' * 30)
print(f'       JOGA NA MEGASENA')
print('-' * 30)
quantos= int(input('Quantos jogos você quer que eu sorteie? '))
tot= 1
while tot <= quantos:
    cont= 0
    while True:
        num= randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1) """