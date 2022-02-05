file_path = r'C:\Users\PC\Documents\GitHub\curso-intensivo-python2\curso-intensivo-python\10_Arquivos_e_excecoes\notas\pi_digits.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line)

    # contents = file_object.read()
    # print(contents)

    # pag 234

#Trabalhando com listas de linha de um arquivo
print('\n')

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    