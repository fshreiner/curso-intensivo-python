# Exemplo simples de condição if
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': # Valida se o conteúdo é BMW, se sim, exibe o valor todo em maiúsculo
        print(car.upper())
    else: # Se não for BMW, usa o title para deixar somente a primeira letra maiúscula
        print(car.title())
