# 6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
# um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
# sequência de instruções print por um laço que percorra as chaves e os valores
# do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
# cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
# essas palavras e significados novos deverão ser automaticamente incluídos na
# saída.
glossary = {
    'lista': 'Permite armazenar um conjunto de dados como se fosse uma pilha de itens',
    'variavel': 'Permite armazenar um valor, um dado, alguma coisa, imitando um objeto da vida real',
    'tupla': 'É como uma lista, porém tem valores fixos, que não podem ser mudados',
    'python': 'Linguagem de programação super poderosa e interativa',
    'dicionario': 'Permite armazenar uma ou várias chaves e associar um valor a cada chave',
    'codigo': 'Comandos e instruções para softwares e aplicações',
    'css': 'Cascata de estilos para web pages',
    'html': 'Linguagem de marcação',
    'git': 'Ferramenta para versionamento de códigos',
    'money': 'O que se ganha ao programar bem',
}

for word, signify in glossary.items():
    print(word.title() + ': ' + signify + '.')
