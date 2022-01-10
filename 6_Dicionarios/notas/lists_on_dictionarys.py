# Armazenando listas em um dicionário, para situações por exemplo em que dois 
# atributos de um item devem ser listados para determinado fim
# Tipo de massa de pizza e ingredientes por exemplo

# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Resume o pedido
print('You ordered a ' + pizza['crust'] + '-crust pizza with the following' +
    ' toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

# Exibindo novamente a lista de linguagens favoritas, mas desta vez permitindo
# a pessoa escolha mais de uma linguagem favorita
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
