# Criando uma lista (listas são indicadas por colchetes [] e os elementos da lista separados por vírgulas)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Acessando elementos de uma lista (é necessário informar a posição ou índice do item desejado seguindo a sequencia da lista, partindo do zero 0)
print(bicycles[0] + "\n")

# É possível utilizar métodos de string ao exibir um valor da lista
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[2].lower() + "\n")

# Python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no índice -1, Python sempre devolve o último item da lista.
# Essa convenção também se estente a outros valores negativos, por exemplo -2 retorna o penúltimo item da lista, e -3 o antepenúltimo.
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
