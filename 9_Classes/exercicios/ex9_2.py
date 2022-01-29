# 9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
# instâncias diferentes da classe e chame describe_restaurant() para cada
# instância.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        print('O restaurante se chama {}'.format(self.restaurant_name.title()) +
            ' e o seu tipo de culinária é {}'.format(self.cuisine_type))

    
    def open_restaurant(self):
        print('O restaurante está aberto!')

restaurant = Restaurant('baratiê', 'pirata')
restaurant2 = Restaurant('spider cafe', 'árabe')
restaurant3 = Restaurant('danlutti', 'italiana')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
