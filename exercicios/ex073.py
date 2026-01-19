brasileirão = 'Flamengo', 'São Paulo', 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Athletico-PR', 'Fluminense', 'Botafogo', 'Fortaleza', 'Grêmio', 'Bahia', 'Internacional', 'América', 'Red Bull Bragantino', 'Vasco', 'Santos', 'Atlético-GO', 'Juventude', 'Cruzeiro', 'Cuiabá'
print('Esses são os cinco primeiros times do Brasileirão atualmente:')
for cont in range(0, 5):
    print(f'{brasileirão[cont]}')

print('\nEsses são os últimos quatro colocados:')
for cont in range(-4, -0):
    print(f'{brasileirão[cont]}')
    
print(f'Esses são os times em ordem alfabética: {sorted(brasileirão)}')

print(f'O vasco está na {brasileirão.index('Vasco')+ 1}° posição')