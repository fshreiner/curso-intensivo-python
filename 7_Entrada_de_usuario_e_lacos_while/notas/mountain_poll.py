responses = {}

# Definir uma flag para indicar que a enquete está ativa
polling_activate = True

while polling_activate:
    # Pede o nome da pessoa e a resposta
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # Armazena a resposta no dicionário
    responses[name] = response

    # Descobre se outra pessoa vai responder a enquete
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_activate = False
    
# A enquete foi concluída. Mostra os resultados
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
