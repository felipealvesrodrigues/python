valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]: #Se o valor for o primeiro inserido ele vai ser primeiro. O mesmo acontece se o valor inserido for maior que o último (em posição mesmo) valor da lista 
        valores.append(n)
    else: # se ele nao for maior, um contador pos vai começar a rodar, pos vai assumir os valores de index, ou seja, quando pos for 0, ele vai valer o valor 0 da lista, e assim sucessivamente.
        pos = 0
        while pos < len(valores): # isso aq vai fazer basicamente o contador rodar, enquanto ele for menor que o tamanho da lista, ele vai aumentar la em baixo, onde ta escrito pos += 1
            if n <= valores[pos]: #se o numero de n for menor igual a algum número da lista(ela está sendo varrida pelo while pos ali) eu vou inserir em alguma posição desejada(isso vai ta nas linhas de baixo)
                valores.insert(pos, n) # aqui, o valor vai ser inserido na posição onde a condição de n ser menor que algum valor da lista for cumprida.
                break # e quando tudo acabar, break
            pos += 1
print(valores)