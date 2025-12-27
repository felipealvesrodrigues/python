""" for c in range(0, 50+1):
    if c % 2 == 0:
        print(c) """
        
for c in range(2, 50+1, 2): # o laço se repete inutilmente algumas vezes, fazendo ele começar do dois e pular de dois em 2 evita isso. Otimização:)
    if c % 2 == 0:
        print(c, end =' ')