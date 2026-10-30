# 3. Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo
# Ejemplo:
#     Entrada:
#         # archivo original:
#         hola mundo
#         esto es python

#     Salida:
#         # archivo nuevo:
#         HOLA MUNDO
#         ESTO ES PYTHON

def read_file_lines_return_list(path):
    with open(path, 'r', encoding='utf-8') as file:
        return [line.rstrip('\n') for line in file.readlines()]

def write_file_with_all_words_uppercase(path, my_list):
    with open(path, 'w', encoding='utf-8') as file:
        for line in my_list:
            file.write(line.upper()+'\n')

def read_file_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines=file.readlines()
        for line in lines:
            print(line.strip())

def get_subfolder_name():
    full_path=__file__
    path_parts = full_path.split('\\')
    return path_parts[-2]

def main():
    try:
        print("hola_mundo.txt (Before converting to uppercase):")
        read_file_lines(f'{get_subfolder_name()}\\hola_mundo.txt')

        my_list = read_file_lines_return_list(f'{get_subfolder_name()}\\hola_mundo.txt')
        write_file_with_all_words_uppercase(f'{get_subfolder_name()}\\hola_mundo_upper.txt', my_list)

        print("")
        print("hola_mundo_upper.txt:")
        read_file_lines(f'{get_subfolder_name()}\\hola_mundo_upper.txt')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()