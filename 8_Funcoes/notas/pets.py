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
