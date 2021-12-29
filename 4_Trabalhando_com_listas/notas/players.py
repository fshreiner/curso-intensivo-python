# Fatiando uma lista: É possível usar uma função para selecionar somente um grupo específico de itens de uma lista, de forma parecida com o range()
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # Usando o range, vamos conseguir exibir somente o especificado, no caso uma fatia da lista de jogadores, retornando os 3 primeiros

# É possível gerar qualquer subconjunto numa lista
print(players[1:4])

# Se não argumentarmos o início da lista, Python vai considerar que seja o primeiro elemento da lista
print(players[:4])

# O mesmo vale para  o fim da lista
print(players[2:])

# Assim, é possível exibir os elementos de uma lista de certo ponto conhecido até seu final, mesmo q o final seja desconhecido

# Exibindo os três últimos elementos usando índice negativo
print(str(players[-3:]) + '\n')

# Percorrendo uma fatia com um laço de repetição
print("Here are the first three players on my team: ")

for player in players[:3]:
    print(player.title())
