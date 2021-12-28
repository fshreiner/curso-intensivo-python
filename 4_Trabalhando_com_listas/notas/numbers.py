# Usando a função range()
# A função range() gera uma série de números para se usar no for, para se exibir uma sequência de números, por exemplo:
for value in range(1,5): # Conta e exibe de 1 a 4, pois quando chega no 5 a função é encerrada antes do comando print abaixo. Para exibir o 5 teria que usar de argumento (1,6)
    print(value)

# Range pode ser usado para criar uma lista também, inserindo o valor da variável atual na lista, por exemplo:
numbers = list(range(1,6))
print(str(numbers) + '\n')

# Podemos também usar range() para dizer para Python ignorar alguns valores, por exemplo mostrar somente os numeros pares de 0 a 10:
even_numbers = list(range(2,11,2))
print(str(even_numbers) + '\n')

# Outro exemplo, números de 0 a 10 elevados ao quadrado perfeito:
squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)

print(str(squares) + '\n')

# Ou outra forma:
squares = []

for value in range(1,11):
    squares.append(value**2)

print(str(squares) + '\n')

# Algumas funções Python são específicas para listas de números. Por
# exemplo, podemos encontrar facilmente o valor mínimo, o valor
# máximo e a soma de uma lista de números:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) # Exibe o menor valor da lista
print(max(digits)) # Exibe o maior valor da lista
print(sum(digits)) # Soma os valores da lista
