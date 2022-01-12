# Usando Break para parar o laço while
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break #  Usando o break
    else:
        print("I'd love to go to {}".format(city.title()) + "!" )
