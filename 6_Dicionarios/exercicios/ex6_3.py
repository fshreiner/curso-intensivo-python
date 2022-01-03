# 6.3 – Glossário: Um dicionário Python pode ser usado para modelar um
# dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
# glossário.
# • Pense em cinco palavras relacionadas à programação que você conheceu
# nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
# armazene seus significados como valores.
# • Mostre cada palavra e seu significado em uma saída formatada de modo
# elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
# significado, ou apresentar a palavra em uma linha e então exibir seu
# significado indentado em uma segunda linha. Utilize o caractere de quebra
# de linha (\n) para inserir uma linha em branco entre cada par palavrasignificado em sua saída.
glossary = {
    'lista': 'Permite armazenar um conjunto de dados como se fosse uma pilha de itens',
    'variavel': 'Permite armazenar um valor, um dado, alguma coisa, imitando um objeto da vida real',
    'tupla': 'É como uma lista, porém tem valores fixos, que não podem ser mudados',
    'python': 'Linguagem de programação super poderosa e interativa',
    'dicionario': 'Permite armazenar uma ou várias chaves e associar um valor a cada chave',
}

print('Lista - {}'.format(glossary['lista']) + '.\n')
print('Variável - {}'.format(glossary['variavel']) + '.\n')
print('Tupla - {}'.format(glossary['tupla']) + '.\n')
print('Python - {}'.format(glossary['python']) + '.\n')
print('Dicionário - {}'.format(glossary['dicionario']) + '.\n')
