# 4. Cree un programa que abra un archivo .csv con la información de 
# videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
#     1. Lea el archivo .csv con videojuegos
#     2. Pida al usuario ingresar el nombre de un desarrollador 
#        (ej. "Ubisoft")
#     3. Muestre todos los videojuegos desarrollados por esa empresa en 
#        formato legible:
#         Ejemplo:
#             Salida:
#                 Videojuegos desarrollados por Ubisoft:
#                 - Assassin's Creed II (Clasificación: M, Género: Aventura)
#                 - Rayman Legends (Clasificación: E, Género: Plataforma)

import csv
from pathlib import Path

FILE_NAME = 'games_details.csv'

def get_csv_as_list_of_dict(file_path):
	with file_path.open('r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		return list(reader)

def read_csv_file_and_print(file_path):
	with file_path.open('r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		for item in reader:
			print(item)

def print_games_by_developer(my_games, developer_name):
	counter=0
	for item in my_games:
		if item['developer'].lower()==developer_name.lower():
			print(f'{item['name']} (ESRB Rating: {item['esrb_rating']}, Genre: {item['genre']})')
			counter+=1
	print(f"There are a total of {counter} games with developer: {developer_name}")

def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name

def main():
	try:
		print("---Available Games: ----")
		read_csv_file_and_print(get_absolute_file_path(FILE_NAME))
		games=get_csv_as_list_of_dict(get_absolute_file_path(FILE_NAME))
		print("")
		developer_name=input("Enter the name of the game's developer: ")
        
		print("")
		print(f"Videogames developed by {developer_name}: ")
		print_games_by_developer(games, developer_name)

		
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()