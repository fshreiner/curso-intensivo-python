# 8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
# camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
# uma camiseta grande e outra média com a mensagem default, e uma camiseta
# de qualquer tamanho com uma mensagem diferente.
def make_shirt(size_shirt='G', text_shirt='Eu amo Python!'):
    print('\nO tamanho da camiseta escolhida foi {}'.format(size_shirt) + 
        ' e a frase para a estampa é: {}'.format(text_shirt))

make_shirt()
make_shirt(size_shirt='M')
make_shirt(text_shirt='Eu amo React!')
