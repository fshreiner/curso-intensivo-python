# Utilizando um valor diferente de, para instrução if
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!\n')

# Testando várias condições
# A cadeia if-elif-else é eficaz, mas é apropriada somente quando você
# quiser que apenas um teste passe. Assim que encontrar um teste que
# passe, o interpretador Python ignorará o restante dos testes. Esse
# comportamento é vantajoso, pois é eficiente e permite testar uma
# condição específica.

# Às vezes, porém, é importante verificar todas as condições de
# interesse. Nesse caso, você deve usar uma série de instruções if simples,
# sem blocos elif ou else. Essa técnica faz sentido quando mais de uma
# condição pode ser True e você quer atuar em todas as condições que
# sejam verdadeiras.
# Vamos reconsiderar o exemplo da pizzaria. Se alguém pedir uma pizza
# com dois ingredientes, será necessário garantir que esses dois
# ingredientes sejam incluídos em sua pizza: 
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'peperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!\n')

# Verificando se existem itens específicos na lista
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding {}'.format(requested_topping.title()) + '.')

print('\nFinished making your pizza!\n')

# Verificando se uma lista está vazia
requested_toppings = []

if requested_toppings: # Ao informar só o nome da lista o sistema valida, se tiver ao menos um item retorna True, se estiver vazia retorna False
    for requested_topping in requested_toppings:
        print('Adding {}'.format(requested_topping.title()) + '.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?\n')

# Usando várias listas
# As pessoas pedirão de tudo, em especial quando se tratar de
# ingredientes para uma pizza. E se um cliente realmente quiser batatas
# fritas em sua pizza? Podemos usar listas e instruções if para garantir que
# o dado de entrada faça sentido antes de atuar sobre ele.
# Vamos prestar atenção em solicitações de ingredientes incomuns antes
# de prepararmos uma pizza. O exemplo a seguir define duas listas. A
# primeira é uma lista de ingredientes disponíveis na pizzaria, e a segunda
# 126
# é a lista de ingredientes que o usuário pediu. 
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding {}'.format(requested_topping) + '.')
    else:
        print('Sorry, we dont have {}'.format(requested_topping) + '.')
print('\nFinished making your pizza!')
