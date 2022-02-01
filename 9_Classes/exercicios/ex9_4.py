# 9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
# 225). Acrescente um atributo chamado number_served cujo valor default é 0.
# Crie uma instância chamada restaurant a partir dessa classe. Apresente o
# número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
# exiba-o novamente.
# Adicione um método chamado set_number_served() que permita definir o
# número de clientes atendidos. Chame esse método com um novo número e
# mostre o valor novamente.
# Acrescente um método chamado increment_number_served() que permita
# incrementar o número de clientes servidos. Chame esse método com qualquer
# número que você quiser e que represente quantos clientes foram atendidos, por
# exemplo, em um dia de funcionamento.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 3

    
    def describe_restaurant(self):
        print('O restaurante se chama {}'.format(self.restaurant_name.title()) +
            ' e o seu tipo de culinária é {}'.format(self.cuisine_type))

    
    def open_restaurant(self):
        print('O restaurante está aberto!')

    def print_clientes_served(self):
        print('Já foram atendidos {}'.format(restaurant.number_served) + 
            ' clientes.')

        
    def set_number_served(self, number_of_clients):
        self.number_served = number_of_clients

    
    def increment_number_served(self, number_of_clients):
        self.number_served += number_of_clients

restaurant = Restaurant('baratie', 'pirata')
print('Já foram atendidos {}'.format(restaurant.number_served) + ' clientes.')

restaurant.set_number_served(40)
restaurant.print_clientes_served()

restaurant.increment_number_served(20)
restaurant.print_clientes_served()

restaurant.increment_number_served(50)
restaurant.print_clientes_served()
