# 6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
# 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
# apresente o nome de cada pessoa, juntamente com seus números favoritos.
favorite_numbers = {
    'lari': [6, 34, 54],
    'fabio': [29, 23, 32, 35],
    'luffy': [13, 23],
    'zoro': [56, 34, 89, 65, 43],
    'sanji': [41, 43, 21],
}

for name, numbers in favorite_numbers.items():
    print('\n\t' + name.title())
    print('Números favoritos: ')
    for number in numbers:
        print('\t' + str(number))
