# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
# acrescente várias linhas no final do programa que façam o seguinte: • Exiba a
# mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
# exibir os três primeiros itens da lista desse programa.
# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
# 102
# três itens do meio da lista.
# • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
# exibir os três últimos itens da lista.

numbers = []

for value in range(1,21):
    numbers.append(value)
    print(value)

print('The first three items on the list are: ')
print(numbers[0:3])

print('The three items in the middle of the list are: ')
print(numbers[9:12])

print('The last three items on the list are: ')
print(numbers[-3:])
