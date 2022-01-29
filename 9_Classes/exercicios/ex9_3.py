# 9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
# first_name e last_name e, então, crie vários outros atributos normalmente
# armazenados em um perfil de usuário. Escreva um método de nome
# describe_user() que apresente um resumo das informações do usuário. Escreva
# outro método chamado greet_user() que mostre uma saudação personalizada
# ao usuário.
# Crie várias instâncias que representem diferentes usuários e chame os dois
# métodos para cada usuário.
from re import A


class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    
    def describe_user(self):
        print('Dados do usuário: ')
        print('\tNome: {}'.format(self.first_name.title()))
        print('\tSobrenome: {}'.format(self.last_name.title()))
        print('\tIdade: {}'.format(self.age))

    def greet_user(self):
        print('Olá, seja bem-vindo(a) {}'.format(self.first_name.title()) + '!')

fabio = User('fabio', 'shreiner', 48)
lari = User('larissa', 'carósio', 45)
amanda = User('amanda carósio', 'shreiner', 18)

fabio.describe_user()
fabio.greet_user()
lari.describe_user()
lari.greet_user()
amanda.describe_user()
amanda.greet_user()
