# Copiando uma lista
# Eventualmente poderemos precisar copiar o índice todo de uma lista para criar uma nova lista e prosseguir a partir dela, desta forma
# podemos usar como índice valores em branco, desta forma: [:] isto indica para se considerar o valor total da lista
# Exemplo:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Indicando assim que ele receberá meus itens no total

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# Provando que são listas distintas
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)


