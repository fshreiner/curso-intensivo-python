# considere um parque de diversões que cobre
# preços distintos para grupos etários diferentes: • a entrada para
# qualquer pessoa com menos de 4 anos é gratuita; • a entrada para
# qualquer pessoa com idade entre 4 e 18 anos custa 5 dólares; • a entrada
# para qualquer pessoa com 18 anos ou mais custa 10 dólares.
# Como podemos usar uma instrução if para determinar o preço da
# entrada de alguém?
age = int(input('Informe a idade: '))

if age < 4:
    print('Your admission cost is $0.\n')
elif age < 18:
    print('Your admission cost is $5.\n')
else:
    print('Your admission cost is $10.\n')


# Em vez de exibir o preço da entrada no bloco if-elif-else, seria mais
# conciso apenas definir o preço na cadeia if-elif-else e, então, ter uma
# instrução print simples que execute depois que a cadeia for avaliada:
age = int(input('Informe a idade: '))

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is ${}'.format(price) + '.\n')

# Podemos usar vários blocos de elif
# se o parque de diversões implementasse um desconto para
# idosos, você poderia acrescentar mais um teste condicional no código a
# fim de determinar se uma pessoa está qualificada a receber esse
# desconto. Suponha que qualquer pessoa com 65 anos ou mais pague
# metade do preço normal da entrada, isto é, 5 dólares:
age = int(input('Informe a idade: '))

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print('Your admission cost is ${}'.format(price) + '.\n')


# Omitindo o bloco else
# Python não exige um bloco else no final de uma cadeia if-elif. Às vezes,
# um bloco else é útil; outras vezes, é mais claro usar uma instrução elif
# adicional que capture a condição específica de interesse:
age = int(input('Informe a idade: '))

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print('Your admission cost is ${}'.format(price) + '.\n')
