# Trabalhando com laços
# O laço for é ótimo para quando se quer fazer uma ação com cada item em uma lista, assim ele evita termos que ficar mudando o código toda hora caso vamos exibir um item da lista por vez manualmente
magicians = ['alice', 'david', 'carolina']

for magician in magicians: # Laço de repetição for: para cada mágico na lista mágicos faça:
    print(magician.title() + ', that was a great trick!') # Exibe na tela o nome do mágico atual armazenado na variável magician com a mensagem proposta
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # Podemos usar quantas linhas quisermos dentro do laço for, toda linha que for indentada no for será executada uma vez para cada item na lista

print("Thank you, everyone. That was a great magic show!") # Como esta linha não está indentada, será executada apenas uma vez
