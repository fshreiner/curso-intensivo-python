# Ordenando uma lista om Python
# É comum que seja necessário ordenar uma lista no dia a dia, independente de vários fatores, como por exemplo ordenar uma lista em ordem alfabética

# Ordenando uma lista com Sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Ordenando a lista com o método sort(), os itens se ordenam em ordem alfabética, a lista será reordenada permanentemente
print(cars)

# Podemos fazer a ordem alfabética reversa, usando o argumento reverse=true
cars.sort(reverse=True) # Lembrando que a lista vai ser novamente reordenada permanentemente
print(cars)

# Para ordenar uma lista temporariamente utilizamos o método sorted()
cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars_2)

print('\nHere is the sorted list:')
print(sorted(cars_2))
print('\nHere is the original list again:')
print(cars_2)

# Nota: Essa função Sorted também pode aceitar o argumento reverse=True para exibir a ordem alfabética reversa

# Exibindo uma lista em ordem inversa
# Para inverter a ordem original da lista basta utilizar o método reverse(), lembrando que ele inverte a ordem da lista original,
# independente da ordem alfabética, permanentemente, porém para retornar ao valor original basta usar o reverse() mais uma vez
print(cars_2)
cars_2.reverse()
print(cars_2)

cars_2.reverse()

# Descobrindo o tamanho de uma lista
# Podemos descobrir rapidamente o tamanho de uma lista usando o método len(), que retorna a quantidade de itens presente na lista
print(len(cars_2))
