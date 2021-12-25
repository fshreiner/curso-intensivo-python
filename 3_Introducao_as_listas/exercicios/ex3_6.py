# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.
# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que
# você encontrou uma mesa de jantar maior.
# 79
# • Utilize insert() para adicionar um novo convidado no início de sua lista.
# • Utilize insert() para adicionar um novo convidado no meio de sua lista.
# • Utilize append() para adicionar um novo convidado no final de sua lista.
# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
# que está em sua lista.

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
print('Hi {}'.format(guests[6].title()) + ', how are you? I invite you to dinner at my house today at 8pm!')
