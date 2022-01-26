# Função que exibe uma saudação
def greet_user(username):
    """"Exibe uma saudação simples."""
    print('Hello, {}'.format(username.title()) + '!')

greet_user('jesse')

# Argumentos e parâmetros
# A variável username na definição da função é um exemplo de parâmetro
# O valor 'jesse' passado a função é um exemplo de argumento. Um argumento é
# uma informação passada para uma função em sua chamada.

# Usando uma função com um laço while
def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formtado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Este é um loop infinito!
while True:
    print('\nPlease tell me your name:')
    print('(enter q at any time to quit)')
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print('\nHello, {}'.format(formatted_name) + '!')
