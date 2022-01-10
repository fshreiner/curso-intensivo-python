# 6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
# (página 147). Crie dois novos dicionários que representem pessoas diferentes e
# armazene os três dicionários em uma lista chamada people. Percorra sua lista
# de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
# você sabe sobre cada pessoa.
person1 = {
    'first_name': 'Fabio',
    'last_name': 'Shreiner',
    'age': 25,
    'city': 'Monte Azul Paulista',
}

person2 = {
    'first_name': 'Monkey D.',
    'last_name': 'Luffy',
    'age': '18',
    'city': 'Vila Fusha',
}

person3 = {
    'first_name': 'Roronoa',
    'last_name': 'Zoro',
    'age': '19',
    'city': 'Vila Shimotsuki',
}

peoples = [person1, person2, person3]

for people in peoples:
    print('\tPrimeiro Nome: {}'.format(people['first_name']))
    print('\tÚltimo Nome: {}'.format(people['last_name']))
    print('\tIdade: {}'.format(people['age']))
    print('\tCidade: {}'.format(people['city']))
    print('\n')
