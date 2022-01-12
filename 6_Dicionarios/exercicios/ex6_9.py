# 6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
# três nomes para usar como chaves do dicionário e armazene de um a três
# 149
# lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
# interessante, peça a alguns amigos que nomeiem alguns de seus lugares
# favoritos. Percorra o dicionário com um laço e apresente o nome de cada
# pessoa e seus lugares favoritos.
favorite_places = {
    'fabio': ['canada', 'londres'],
    'lari': ['jalapeno', 'japão', 'amazonia'],
    'gregory': ['disney'],
}

for name, places in favorite_places.items():
    print('\nNome do entrevistado: {}'.format(name.title()))
    print('Lugares favoritos:')
    for place in places:
        print('\t' + place.title())
