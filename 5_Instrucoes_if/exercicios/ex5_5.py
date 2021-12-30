# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
# em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador
# ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o
# jogador ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o
# jogador ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja
# exibida para a cor apropriada do alienígena.
alien_color = 'red'
alien2_color = 'green'
alien3_color = 'yellow'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
    
print('Você acabou de ganhar {}'.format(points) + ' pontos\n')

if alien2_color == 'green':
    points = 5
elif alien2_color == 'yellow':
    points = 10
elif alien2_color == 'red':
    points = 15
    
print('Você acabou de ganhar {}'.format(points) + ' pontos\n')

if alien3_color == 'green':
    points = 5
elif alien3_color == 'yellow':
    points = 10
elif alien3_color == 'red':
    points = 15
    
print('Você acabou de ganhar {}'.format(points) + ' pontos')
