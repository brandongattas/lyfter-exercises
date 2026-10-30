# 1. Cree un programa que abra un archivo .csv con la información de 
# videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea
# Ejemplo:
#     Salida:
#         Nombre: Grand Theft Auto IV
#         Género: Accion
#         Desarrollador: Rockstar Games
#         Clasificación: M

import csv
import os

FILE_NAME='games_details.csv'

def read_csv_file_and_print(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.DictReader(file)

        for item in reader:
            print("--------------")
            for key, value in item.items():
                print(f"{key}: {value}")

def get_absolute_file_path(file_name):
	script_dir = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(script_dir, file_name)


def main():
    try:
        read_csv_file_and_print(get_absolute_file_path(FILE_NAME))
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()