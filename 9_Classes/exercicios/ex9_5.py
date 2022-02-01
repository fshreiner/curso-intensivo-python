# 9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
# sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
# increment_login_attempts() que incremente o valor de login_attempts em 1.
# Escreva outro método chamado reset_login_attempts() que reinicie o valor de
# login_attempts com 0.
# Crie uma instância da classe User e chame increment_login_attempts()
# várias vezes. Exiba o valor de login_attempts para garantir que ele foi
# incrementado de forma apropriada e, em seguida, chame
# reset_login_attempts(). Exiba login_attempts novamente para garantir que
# seu valor foi reiniciado com 0.
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    
    def describe_user(self):
        print('Dados do usuário: ')
        print('\tNome: {}'.format(self.first_name.title()))
        print('\tSobrenome: {}'.format(self.last_name.title()))
        print('\tIdade: {}'.format(self.age))

    def greet_user(self):
        print('Olá, seja bem-vindo(a) {}'.format(self.first_name.title()) + '!')

    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    
    def reset_login_attempts(self):
        self.login_attempts = 0


fabio = User('fabio', 'shreiner', 25)

fabio.increment_login_attempts()
print(fabio.login_attempts)
fabio.increment_login_attempts()
print(fabio.login_attempts)
fabio.increment_login_attempts()
print(fabio.login_attempts)
fabio.increment_login_attempts()
print(fabio.login_attempts)
fabio.increment_login_attempts()
print(fabio.login_attempts)
fabio.increment_login_attempts()
print(fabio.login_attempts)

fabio.reset_login_attempts()
print(fabio.login_attempts)
