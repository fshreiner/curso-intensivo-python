# 8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
# tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
# A função deve exibir uma frase que mostre o tamanho da camiseta e a
# mensagem estampada.
# Chame a função uma vez usando argumentos posicionais para criar uma
# camiseta. Chame a função uma segunda vez usando argumentos nomeados.
def make_shirt(size_shirt, text_shirt):
    print('\nO tamanho da camiseta escolhida foi {}'.format(size_shirt) + 
        ' e a frase para a estampa é: {}'.format(text_shirt))

make_shirt('GG', 'Go Gryffindor')

make_shirt(size_shirt='XGG', text_shirt='Go program!')
