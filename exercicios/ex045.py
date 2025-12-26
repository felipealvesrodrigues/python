import random
op1 = 'pedra'
op2 = 'papel'
op3 = 'tesoura'
lista = [op1, op2, op3]
computador = random.choice(lista)
escolha = str(input('Pedra, papel ou tesoura? '))
if escolha == 'tesoura' and computador == 'pedra':
    print('O computador escolheu {} e você escolheu {}, \033[31mvocê perdeu bobão.\033[m'.format(computador, escolha))
elif escolha == 'pedra' and computador == 'papel':
    print('O computador escolheu {} e você escolheu {}, \033[31mvocê perdeu bobão.\033[m'.format(computador, escolha))
elif escolha == 'papel' and computador == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, \033[31mvocê perdeu bobão.\033[m'.format(computador, escolha))
elif escolha == 'tesoura' and computador == 'papel':
    print('O computador escolheu {} e você escolheu {}, \033[32mvocê ganhou, parabéns!!\033[m'.format(computador, escolha)) 
elif escolha == 'pedra' and computador == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, \033[32mvocê ganhou, parabéns!!\033[m'.format(computador, escolha)) 
elif escolha == 'papel' and computador == 'pedra':
    print('O computador escolheu {} e você escolheu {}, \033[32mvocê ganhou, parabéns!!\033[m'.format(computador, escolha)) 
    

    
