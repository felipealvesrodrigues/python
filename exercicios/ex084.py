temp= list()
principal= list()
maior= menor= 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior= menor= temp[1]
    else:
        if temp[1] > maior:# eu não preciso de um contador aqui pq como lá em baixo ta dando clear no temp, sempre vai ter só 1 pessoas com os dois dados cadastrados. genial
            maior= temp[1]
        if temp[1] < menor:
            menor= temp[1]
    principal.append(temp[:])
    temp.clear()
    resp= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        resp= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')  
print(f'O maior peso foi de {maior}Kg. Peso de ', end= '')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end= '')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end= '')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end= '')
print()

