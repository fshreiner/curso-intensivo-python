# Exemplos de uso de métodos declarados após a variável, estes úteis quando um título deve ser exibido, ou um dado deve ser colhido todo com letras maiúsculas ou minúsculas.

name = "ada lovelace"

print(name.title()) # Exibe o conteúdo com a primeira letra maiúscula
print(name.upper()) # Exibe o conteúdo com todas letras maiúsculas
print(name.lower()) # Exibe o conteúdo com todas letras minúsculas

first_name = "ada"
last_name = "lovelace"

# Concatenação de strings
full_name = first_name + " " + last_name

# Tabulação e quebra de linhas utilizando /t e /n
print("\t" + full_name)
print("\t" + full_name)
print("\t" + full_name)
print("\t" + full_name)

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Remoção de espaços em branco utilizando o comando strip(remove todo espaço em branco), rstrip(remove espaços em branco a direita) ou lstrip(remove espaços em branco a esquerda)
favorite_language = ' python '

print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
