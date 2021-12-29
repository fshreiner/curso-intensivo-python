# 4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
# de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
# • Use um laço for para exibir cada prato oferecido pelo restaurante.
# • Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
# • O restaurante muda seu cardápio, substituindo dois dos itens com pratos
# diferentes. Acrescente um bloco de código que reescreva a tupla e, em
# seguida, use um laço for para exibir cada um dos itens do cardápio
# revisado.

dishes = ('fricassê de frango', 'escondidinho de carne seca', 'carne ao molho madeira', 'arroz tropeiro', 'macarrão ao forno')

for dish in dishes:
    print('Prato: {}'.format(dish))

dishes = ('fricassê de frango', 'salgados', 'carne ao molho madeira', 'arroz tropeiro', 'empada')

for dish in dishes:
    print('Prato: {}'.format(dish))
