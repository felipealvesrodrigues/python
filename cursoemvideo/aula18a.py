"""pessoas= {'nome': 'Felipe', 'sexo': 'M', 'idade': '18'}
#print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome']= 'Vermesson' eu posso simplesmente substituir asssim :)
pessoas['peso']= 999.90989
for k, v in pessoas.items():
    print(f'{k}= {v}') 
"""

"""
brasil= list()
estado1= {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2= {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
"""

estado= dict()
brasil= list()
for c in range(0, 3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla: '))
    brasil.append(estado.copy()) # eu tenho que fazer um cópia c n fica tudo torto, mas eu tbm n posso usar o fatiamento [:]. Tem q usar o método copy()
for e in brasil:
    #for k, v in e.items():
    #    print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end= ' ')
    print()