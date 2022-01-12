# 6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
# cidades como chaves em seu dicionário. Crie um dicionário com informações
# sobre cada cidade e inclua o país em que a cidade está localizada, a
# população aproximada e um fato sobre essa cidade. As chaves do dicionário
# de cada cidade devem ser algo como country, population e fact. Apresente o
# nome de cada cidade e todas as informações que você armazenou sobre ela.
cities = {
    'londres': {
        'pais': 'inglaterra',
        'populacao': 8982000,
        'fato': 'Em Londres acontecem mais de 17.000 shows por ano, em mais ' +
             'de 300 localidades diferentes. São muitas atrações!',
    },

    'paris': {
        'pais': 'frança',
        'populacao': 2161000,
        'fato': 'Você sabia que todos os anos Paris recebe mais de 40 milhões' +
        ' de visitantes?' ,
    },

    'nova york': {
        'pais': 'estados unidos',
        'populacao': 8419000,
        'fato': 'Nova York já foi cenário para mais de 20 mil filmes, desde '+
         '1908.',
    }, 
}

for citie, citie_info in cities.items():
    print('\n' + citie.title())
    pais = citie_info['pais']
    populacao = citie_info['populacao']
    fato = citie_info['fato']

    print('\tPaís: {}'.format(str(pais).title()))
    print('\tPopulação: {}'.format(str(populacao).title()))
    print('\tFato Curioso: {}'.format(str(fato).title()))
