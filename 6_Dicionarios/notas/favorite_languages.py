favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is {}".format(favorite_languages['sarah'].title()) + '.\n')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".\n")

# Percorrendo todas as CHAVES de um dicionário com um laço
# Quando não necessitamos buscar o valor, podemos trazer só a chave
for name in favorite_languages.keys(): # usando o método .keys()
    print(name.title())
    
# Usando if para propor ações para determinados nomes no dicionário
print('\n')
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# Validando se determinada pessoa respondeu a enquete, se consta no dicionário
if 'erin' not in favorite_languages.keys():
    print('\nErin, please take our poll\n')

# Percorrendo as chaves de um dicionário em ORDEM usando um laço
# Podemos usar a função sorted() para obter uma cópia ordenada das chaves:
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Percorrendo todos os VALORES de um dicionário com um laço
# Da mesma forma que buscamos somente as chaves especificamente, podemos também
# chamar só os valores de um dicionário
print('\nThe following languages have been mentioned: ')
for language in favorite_languages.values():
    print(language.title())

# Trazendo todos valores de forma a não repetir caso um valor seja igual a 
# outro, podemos usar um conjunto(set), que é semelhante a uma lista, exceto 
# que cada item de um conjunto deve ser único
print('\nThe following languages have been mentioned: ')
for language in set(favorite_languages.values()): # só inserir um set()
    print(language.title())
