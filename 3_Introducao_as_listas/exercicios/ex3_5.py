# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.
# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não
# poderá comparecer.
# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.
# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

guests = ['Larissa Carósio', 'Paulo Moura', 'Edu Ribeiro', 'Rodrigo Banha']

print('Hi {}'.format(guests[0].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[1].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[2].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[3].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')

print('Unfortunately {}'.format(guests[3].title()) + ' will not be able to attend the dinner.')

guests[3] = 'Ajurinã Zuwarg' # Substituindo o convidado Rodrigo Banha pelo Ajurinã Zuwarg

print('Hi {}'.format(guests[0].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[1].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[2].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[3].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
