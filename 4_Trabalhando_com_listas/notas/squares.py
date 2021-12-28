# List comprehensions
# Abrangência de lista: gera uma lista de valores com menos código, combinando o laço for e a criação de novos elementos em uma linha, 
# e concatena cada novo elemento automaticamente.

# Lista de quadrados perfeitos com list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
