#Guanabara
expr= str(input('Digite a expressão: '))
#toda expressão pe uma lista, então da pra usar um for para verificar cada caractere dela.
pilha= list()
for símbolo in expr:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop
        else: 
            pilha.append(')')
            break 
        # cada vez q eu abro u parêntese um parêntese é adicionado na pilha, quando um parêntese de fechamento é encontrado, ele vai remover um parêntese q foi aberto da pilha, isso é, ele vai ter encontrado seu par, caso a pilha estiver vazia, ele vai colocar um parêntese fechando e vai dar break, dando um erro
if len(pilha) == 0: # se isso acontece, é pq cada parentese aberto achou seu par, mostrando q a expressão ta certa
    print('Sua expressão é válida')
else: 
    print('Sua expressão não é válida ')