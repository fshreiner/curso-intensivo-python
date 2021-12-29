# Tuplas
# As listas funcionam bem para armazenar conjuntos de itens que podem mudar durante a vida de um programa. 
# A capacidade de modificar listas é particularmente importante quando trabalhamos com uma lista de usuários em um site ou com uma lista de personagens em um jogo. 
# No entanto, às vezes, você vai querer criar uma lista de itens que não poderá mudar. 
# As tuplas permitir fazer exatamente isso. Python refere-se a valores que não podem mudar como imutáveis, e uma lista imutável é chamada de tupla.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Sobrescrevendo uma tupla
# Embora não seja possível modificar uma tupla, podemos atribuir um novo valor a uma variável que armazena uma tupla. 
dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
        