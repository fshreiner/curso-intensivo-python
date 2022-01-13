# Argumentos posicionais
# Argumentos são passados na chamada da função na ordem dos parâmetros
def describe_pet(animal_type, pet_name):
    """"Exibe informações de um animal de estimação"""
    print('\nI have a {}'.format(animal_type) + '.')
    print('My {}'.format(animal_type) +
         "'s name is {}".format(pet_name.title()) + ".")

describe_pet('hamster', 'harry')

# Várias chamadas de função
# Podemos chamar a função quantas vezes forem necessárias
describe_pet('dog', 'willie')

# Argumentos nomeados
# Para evitar confusão na hora de passar a ordem dos argumentos, podemos usar
# pares nome-valor nos parâmetros da função, vamos reescrever a chamada da 
# função, mas dessa vez nomeando os argumentos
describe_pet(animal_type='hamster', pet_name='harry')

# Valores default
# Podemos deixar um valor pré programado para os parâmetros descritos na função,
# assim, caso o argumento não seja passado, o valor default é usado no lugar
# Vamos criar uma describe_pets2 com animal_type com dog de default
def describe_pet2(pet_name, animal_type='dog'):
    """"Exibe informações de um animal de estimação"""
    print('\nI have a {}'.format(animal_type) + '.')
    print('My {}'.format(animal_type) +
         "'s name is {}".format(pet_name.title()) + ".")

describe_pet2(pet_name='willie') # Informamos aqui só o pet_name

describe_pet2(pet_name='bellatrix', animal_type='cat') # Se informamos o 
#tipo do animal, ele assume o valor passado, ignorando o default 
