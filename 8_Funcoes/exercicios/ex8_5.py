# 8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
# nome de uma cidade e seu país. A função deve exibir uma frase simples, como
# Reykjavik está localizada na Islândia. Forneça um valor default ao
# parâmetro que representa o país. Chame sua função para três cidades
# diferentes em que pelo menos uma delas não esteja no país default.
def describe_city(city_name, city_country='default'):
    print('\n{}'.format(city_name.title()) + 
        ' está localizada na {}'.format(city_country.title()))

describe_city('Londres')
describe_city(city_name='Paris')
describe_city(city_name='São Paulo', city_country='Brasil')
