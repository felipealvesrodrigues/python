""" valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    else:
        if continua == 'N':
            break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse= True)
print(f'Os valores em ordem descrescente são {valores}')
pos = 0
while pos < len(valores):
    if valores[pos] == 5:
        print('O valor 5 foi encontrado')
        pos += 1
    else:
        if 5 not in valores:
            print('O valor 5 não foi encontrado')
            break
    
     """
     
#Solução do Guanabara:
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print('-=' * 20)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse= True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista!')