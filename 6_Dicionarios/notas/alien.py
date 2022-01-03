# Um dicionário simples
alien_0 = {
    'color': 'green',
    'points': 5
    }

print(alien_0['color'])
print(alien_0['points'])


# Trabalhando com dicionários
# Acessando valores em um dicionário
# Se um jogador atingir esse alienígena, podemos consultar quantos pontos
# ele deve ganhar usando um código como este:
new_points = alien_0['points']

print('\nYou just earned ' + str(new_points) + ' points!\n')

# Adicionando novos pares chave-valor
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Começando com um dicionário vazio
alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modificando valores em um dicionário
print('\nThe alien is {}'.format(alien_0['color']) + '.')

alien_0['color'] = 'yellow' # Modificando o valor de color

print('\nThe alien is now {}'.format(alien_0['color']) + '.\n')

# Outro exemplo
# Para ver um exemplo mais interessante, vamos monitorar a posição de
# um alienígena que pode se deslocar com velocidades diferentes.
# Armazenaremos um valor que representa a velocidade atual do
# alienígena e, então, usaremos esse valor para determinar a distância que
# o alienígena deve se mover para a direita: 
alien_0 = {
    'color': 'red',
    'points': 5,
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}

print('Original x-position: {}'.format(str(alien_0['x_position'])))
# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua 
# velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alien rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: {}'.format(str(alien_0['x_position'])))

# Removendo pareschave-valor
# Quando não houver mais necessidade de uma informação armazenada
# em um dicionário, podemos usar a instrução del para remover
# totalmente um par chave-valor. Tudo de que del precisa é do nome do
# dicionário e da chave que você deseja remover.
print(alien_0)

del alien_0['points']

print(alien_0)
