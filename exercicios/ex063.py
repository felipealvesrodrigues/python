n = int(input('Quantos números da sequência você deseja mostrar? '))
t1 = 0
t2 = 1
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end= ' -> ')
    t1 = t2 
    t2 = t3
    c += 1
print('FIM')
    