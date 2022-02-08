from operator import truediv
from name_function import get_formatted_name

print('Pressione "q" para sair a qualquer momento.')
while True:
    first = input('\nPrimeiro nome: ')
    if first == 'q':
        break
    last = input('Sobrenome: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('Nome completo: ' + formatted_name + '.')
