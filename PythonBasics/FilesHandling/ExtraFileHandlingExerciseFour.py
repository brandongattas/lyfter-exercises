# 4. Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente
# Ejemplo:
#     Entrada:
#         "Este es un nuevo registro"
    
# Salida:
#         "El texto se agrega al final del archivo sin borrar lo anterior"

def add_data_at_end_of_file(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.write('\n'+data)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content=file.read()
        print(content)

def get_subfolder_name():
    full_path=__file__
    path_parts = full_path.split('\\')
    return path_parts[-2]

def main():
    try:
        file_name=input("Ingrese el nombre del archivo que desea editar: ")
        extra_data=input("Ingrese data que desea agregar al archivo: ")
        add_data_at_end_of_file(f"{get_subfolder_name()}\\{file_name}.txt", extra_data)

        print("")
        print(f"Edited file content - {file_name}.txt")
        read_file(f"{get_subfolder_name()}\\{file_name}.txt")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()