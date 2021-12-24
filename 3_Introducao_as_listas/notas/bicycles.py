# Criando uma lista (listas são indicadas por colchetes [] e os elementos da lista separados por vírgulas)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Acessando elementos de uma lista (é necessário informar a posição ou índice do item desejado seguindo a sequencia da lista, partindo do zero 0)
print(bicycles[0] + "\n")

# É possível utilizar métodos de string ao exibir um valor da lista
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[2].lower() + "\n")

# Python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no índice -1, Python sempre devolve o último item da lista.
# Essa convenção também se estente a outros valores negativos, por exemplo -2 retorna o penúltimo item da lista, e -3 o antepenúltimo.
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3] + "\n")

# Usando valores individuais de uma lista
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message + "\n")

# Alterando um valor na lista, para isto devemos inserir normalmente sua posição, como se fossemos selecionar o elemento, e na frente informar o novo valor
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adicionando um novo elemento na lista, possível através da concatenação do elemento (comando append), em que o novo elemento irá para o final da lista
motorcycles.append('harley davidson')
print(motorcycles)

# Também é possível adicionar elementos escolhendo em qual posição da lista você quer inserí-lo, usando o comando .insert e especificando em qual posição o valor deve ser inserido
motorcycles.insert(0, 'honda')
motorcycles.insert(2, 'dafra')
print(motorcycles)

# Removendo elementos de uma lista, é possível através do comando del (caso a posição do item que voc~e quer remover seja conhecida)
# O comando del exclui o item da lista definitivamente, desta forma o valor fica permanentemente inacessível
del motorcycles[0] # Indica que é para remover o primeiro item da lista, no caso honda
print(str(motorcycles) + "\n")

# Removendo um item com o método pop(), as vezes vai ser necessário utilizar novamente a informação contida no item removido, desta forma o método pop permite remover mas recuperar o
# valor, para ser reutilizado em outras situações, como se fosse uma pilha lógica, removendo o item do topo da pilha, no caso o último item da lista
popped_motorcycles = motorcycles.pop() # Variável recebe o valor do item removido
print(motorcycles) # Exibe a lista atual, com o valor já removido
print(popped_motorcycles) # Exibe o valor removido

# É possível usar o .pop() para remover qualquer item da lista se incluir o índice do item entre parênteses
print(motorcycles) # Exibindo a lista atual de motocicletas
first_owned = motorcycles.pop(0) # Nos parênteses do pop inseri o valor 0, ou seja, vou remover o primeiro item da lista e armazená-lo na variável
print('The first motorcycle I owned was a ' + first_owned.title() + '.\n')

# Remover o item de acordo com o valor, caso você não saiba a posição do valor que quer remover, mas saiba qual o valor contido, pode usar o método remove() para localizar o item
print(motorcycles) # Exibo a lista atual
motorcycles.remove('yamaha') # Removo o item YAMAHA
print(motorcycles) # Exibo a lista atual

# Utilizando o valor removido com o remove() para outras situações
too_expensive = 'suzuki' # Defino uma variável com o valor do item que quero remover
motorcycles.remove(too_expensive) # Digo para o sistema remover o item que esteja na lista que seja igual ao valor da variável
print(motorcycles) # Exibo a lista sem o valor SUZUKI
print("\nA {}".format(too_expensive.title()) + " is too expensive for me.") # A variável continua com o valor do item mesmo após ele ter sido removido, pois foi definido no início do código

# Nota: o método remove apaga somente a primeira ocorrência do valor na lista, caso haja possibilidade de existir mais de um valor na lista com o mesmo nome, é necessário fazer
# um laço de repetição, para garantir que todos valores da lista com o valor especificado sejam removidos.
