# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
# dois convidados.
# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas
# pessoas para o jantar.
# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
# que apenas dois nomes permaneçam em sua lista. Sempre que remover um
# nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
# saiba que você sente muito por não poder convidá-la para o jantar.
# • Apresente uma mensagem para cada uma das duas pessoas que continuam
# na lista, permitindo que elas saibam que ainda estão convidadas.
# • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
# tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
# uma lista vazia no final de seu programa.

guests = ['Larissa Carósio', 'Paulo Moura', 'Edu Ribeiro', 'Rodrigo Banha']

print('Hi {}'.format(guests[0].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[1].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[2].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[3].title()) + ', how are you? I invite you to dinner at my house today at 8pm!\n')

print('Unfortunately {}'.format(guests[3].title()) + ' will not be able to attend the dinner.\n')

guests[3] = 'Ajurinã Zuwarg' # Substituindo o convidado Rodrigo Banha pelo Ajurinã Zuwarg

print('Hi {}'.format(guests[0].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[1].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[2].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[3].title()) + ', how are you? I invite you to dinner at my house today at 8pm!\n')

print('Hi everyone, I would like to inform you that I have found a bigger table and I will be calling some more guests\n')

guests.insert(0, 'Oscar Aldama')
guests.insert(3, 'Joander Simplício')
guests.append('Sérgio Frigério')

print('Hi {}'.format(guests[0].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[1].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[2].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[3].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[4].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[5].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
print('Hi {}'.format(guests[6].title()) + ', how are you? I invite you to dinner at my house today at 8pm!\n')

print("Good afternoon, unfortunately the table won't arrive on time, and I'll only be able to invite two people :(\n")

uninvited_guest_1 = guests.pop(0)
print("Hi {}".format(uninvited_guest_1) + ", unfortunately I won't be able to invite you to dinner anymore, I'm sorry!")

uninvited_guest_2 = guests.pop(1)
print("Hi {}".format(uninvited_guest_2) + ", unfortunately I won't be able to invite you to dinner anymore, I'm sorry!")

uninvited_guest_3 = guests.pop(1)
print("Hi {}".format(uninvited_guest_3) + ", unfortunately I won't be able to invite you to dinner anymore, I'm sorry!")

uninvited_guest_4 = guests.pop(2)
print("Hi {}".format(uninvited_guest_4) + ", unfortunately I won't be able to invite you to dinner anymore, I'm sorry!")

uninvited_guest_5 = guests.pop(2)
print("Hi {}".format(uninvited_guest_5) + ", unfortunately I won't be able to invite you to dinner anymore, I'm sorry!\n")

print('Hi {}'.format(guests[0]) + ' I would like to remind you and confirm that you are still invited to my dinner :)')
print('Hi {}'.format(guests[1]) + ' I would like to remind you and confirm that you are still invited to my dinner :)')

del guests[0]
del guests[0]

print(guests)
