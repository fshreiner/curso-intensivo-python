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

print('\nFinished making your pizza!')
 
