# 7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
# de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
# ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
# dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
# informe-lhes o preço do ingresso do cinema.

message = "Informe a idade do cliente: "
message += "\n(Digite '999' para finalizar o sistema)"

flag = True

while flag == True:
    age = int(input(message))
    if age == 999:
        flag = False
    elif age < 3:
        print('Entrada gratuita.\n')
    elif age <= 12:
        print('Preço: 10$\n')
    elif age > 12:
        print('Preço = 15$\n')
