# 6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
# dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
# o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
# chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
# fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
ace = {
    'type': 'dog',
    'owner': 'fabio',
}

narciso = {
    'type': 'cat',
    'owner': 'fabio',
}

bellatrix = {
    'type': 'cat',
    'owner': 'shreiner',
}

fawkes = {
    'type': 'bird',
    'owner': 'henrique',
}

pets = [ace, narciso, bellatrix, fawkes]

for pet in pets:
    print('Animal: {}'.format(pet))
    print('Tipo do Animal: {}'.format(pet['type']))
    print('Dono do Animal: {}'.format(pet['owner']))
    print('\n')
