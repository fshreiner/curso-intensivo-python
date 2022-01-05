# Uma lista de dicionários
# Como armazenar informações sobre uma frota alienígena? Com uma lista, 
# contendo dicionários!
alien_0 = {
    'color': 'green',
    'points': 5
}

alien_1 = {
    'color': 'yellow',
    'points': 10
}

alien_2 = {
    'color': 'red',
    'points': 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n')

# -----------------------------------------------------------------------------
# Um outro exemplo, criando uma frota de 30 alienígenas
# Lista vazia para armazenar os aliens
aliens = []

# Criando 30 aliens verdes
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

# Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
    print('...')

# Mostra quantos alienígenas foram criados
print('Total number of aliens: ' + str(len(aliens)) + '\n')

#------------------------------------------------------------------------------
# Alterando propriedades de alguns destes aliens, por exemplo, os 3 primeiros
# ganham upgrade para amarelo, velocidade média e valem 10 pontos, como 
# realizar a alteração?
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Mostra novamente os 5 primeiros
for alien in aliens[:5]:
    print(alien)
    print('...')

print('\n')

# Agora transformando os aliens amarelos em vermelhos
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Mostra novamente os 5 primeiros
for alien in aliens[:5]:
    print(alien)
    print('...')
