v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair')
    escolha = int(input('Faça sua escolha: '))
    if escolha == 1:
        print(v1 + v2)
    elif escolha == 2:
        print(v1 * v2)
    elif escolha == 3:
        if v1 > v2:
            print(v1)
        else:
            print(v2)
    elif escolha == 4:
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
print('Fim')
    