# 6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
# • Crie uma lista de pessoas que devam participar da enquete sobre linguagem
# favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
# estão.
# 143
# • Percorra a lista de pessoas que devem participar da enquete. Se elas já
# tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
# responder. Se ainda não participaram da enquete, apresente uma mensagem
# convidando-as a responder.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

list_of_participants = [
    'fabio',
    'edward',
    'lari',
    'jen',
    'gui',
    'will',
    'kaio',
    'zoro',
    'jinbei',
    'sarah',
    'edward',
    'alphonse',
    'bernardo',
    'miguel',
    'phil',
]

for name in list_of_participants:
    if name in favorite_languages.keys():
        print('Obrigado por participar, {}'.format(name.title()) + '!')
    else:
        print('Por gentileza {}'.format(name.title()) + 
            ', responda o questionário.')
