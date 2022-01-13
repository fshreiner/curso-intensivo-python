# Função que exibe uma saudação
def greet_user(username):
    """"Exibe uma saudação simples."""
    print('Hello, {}'.format(username.title()) + '!')

greet_user('jesse')

# Argumentos e parâmetros
# A variável username na definição da função é um exemplo de parâmetro
# O valor 'jesse' passado a função é um exemplo de argumento. Um argumento é
# uma informação passada para uma função em sua chamada.
