# 8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
# um parâmetro title. A função deve exibir uma mensagem como Um dos meus
# livros favoritos é Alice no país das maravilhas. Chame a função e não se
# esqueça de incluir o título do livro como argumento na chamada da função.
def favorite_book(title):
    """"Exibe o livro favorito digitado pela pessoa"""
    print('Um dos meus livros favoritos é: {}'.format(title.title()))

title = input("Informe um dos seus livros favoritos: ")

favorite_book(title)
