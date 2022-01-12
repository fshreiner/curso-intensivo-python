current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# Usando continue em um laço
print('\nÍmpares de 0 a 10')

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # Continue ignora o resto do código e volta ao início

    print(current_number)
